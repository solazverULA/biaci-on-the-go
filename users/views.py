# users/views.py
from django.shortcuts import render , redirect
from django.views.generic import TemplateView
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm
from .models import CompleteUser, CustomUser , RegistedUserId
from consulta.models import Consulta
from django.template.response import TemplateResponse
from django.views.generic import View, CreateView

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
        context = {'consulta' : Consulta.objects.raw('''SELECT 1 as id, titulo, cota, tipo_material, COUNT(titulo) as total
                                                        FROM consulta_consulta
                                                        GROUP BY titulo, cota, tipo_material
                                                        ORDER BY total
                                                        DESC LIMIT 10'''),}
        return TemplateResponse(request, 'home.html', context)


def PerfilView(request):
	if request.method == "GET" and request.user.is_authenticated and request.user.is_superuser == False:
		usuario = CustomUser.objects.get(username=request.user)
		userdata = CompleteUser.objects.get(customuser_ptr_id=usuario.id)
		return render(request,'perfil.html',{'userdata':userdata},)
	else:
		return redirect('login')

class ErrorSignUp(View):

    """
    """
    def get(self, request):
        return TemplateResponse( request ,'error_signup.html')



# Create your views here.

def Sugerencias(request):
        context = {'consulta' : Consulta.objects.raw('''SELECT *
                                                        FROM consulta_consulta                                                   
                                                        DESC LIMIT 3'''),}
        return TemplateResponse(request, 'Sugerencias.html', context)
