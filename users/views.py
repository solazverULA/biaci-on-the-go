# users/views.py
from django.shortcuts import render , redirect
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from .models import CompleteUser, CustomUser
from consulta.models import Consulta
from django.template.response import TemplateResponse

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def HomePageView(request):
        context = {'consulta' : Consulta.objects.raw('''SELECT 1 as id, titulo, COUNT(titulo) as total
                                                        FROM consulta_consulta
                                                        GROUP BY titulo
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
# Create your views here.
