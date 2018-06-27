# users/views.py
from django.shortcuts import render , redirect
from django.views.generic import TemplateView
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm
from .models import CompleteUser, CustomUser , RegistedUserId
from consulta.models import Consulta
from django.template.response import TemplateResponse
from django.views.generic import View, CreateView
from django.db.models import Count , Max
from prestamo.models import Prestamo

from datetime import datetime, timezone, timedelta # Para obtener el tiempo actual


class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    def form_valid(self, form):
        if (RegistedUserId.objects.filter(cedula=form.instance.cedula).exists()):
            return super(SignUp, self).form_valid(form)
        else:
            return redirect('error_signup')




def HomePageView(request):
    tema = Consulta.objects.filter(username=request.user)[:5]
    if tema.exists() == True:
        for temas in tema.all():
            tema_consultado = temas.tema
            tema_repite = Consulta.objects.filter(tema=tema_consultado).annotate(num=Count(temas.id)).aggregate(max=Max('num'))
        context = {'querys' : tema_repite,
                    'consulta' : Consulta.objects.raw('''SELECT 1 as id, titulo, cota, tipo_material, COUNT(titulo) as total
                                                                            FROM consulta_consulta
                                                                            GROUP BY titulo, cota, tipo_material
                                                                            ORDER BY total
                                                                            DESC LIMIT 10'''),
        }
        return TemplateResponse(request, 'home.html', context)

    context = {'consulta' : Consulta.objects.raw('''SELECT 1 as id, titulo, cota, tipo_material, COUNT(titulo) as total
                                                        FROM consulta_consulta
                                                        GROUP BY titulo, cota, tipo_material
                                                        ORDER BY total
                                                        DESC LIMIT 10'''),
                                                        }
    return TemplateResponse(request, 'home.html', context)


def PerfilView(request):
    """
    Funcion que muestra el perfil del usuario, ademas consulta si tiene prestamos proximos a vencerse para notificarlo
    :param request:
    :return: Render
    """
    if request.method == "GET" and request.user.is_authenticated and request.user.is_superuser == False:
        usuario = CustomUser.objects.get(username=request.user)
        userdata = CompleteUser.objects.get(customuser_ptr_id=usuario.id)
        # Consulto prestamos que no se han vencido
        hoy = datetime.now(timezone.utc)
        prestamos = Prestamo.objects.filter(fecha_entrega__gte=hoy, id_usuario=request.user)
        if prestamos.exists() == True:
            for prestamo in prestamos.all():
                # Obtengo fechas de 3 dias antes para enviar la notificacion
                dias = timedelta(days=3)
                fecha_empieza = prestamo.fecha_entrega - dias
                if str(hoy) >= str(fecha_empieza) and str(hoy) <= str(prestamo.fecha_entrega):
                    return render(request, 'perfil.html', {'userdata': userdata, 'prestamo': prestamos}, )
                else:
                    return render(request, 'perfil.html', {'userdata': userdata, 'prestamo': 0}, )
        else:
            return render(request, 'perfil.html', {'userdata': userdata, 'prestamo': 0}, )
    else:
        return redirect('login')


class ErrorSignUp(View):

    """
    """
    def get(self, request):
        return TemplateResponse( request ,'error_signup.html')
