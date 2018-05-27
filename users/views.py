# users/views.py
from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from .models import CompleteUser, CustomUser

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class HomePageView(TemplateView):
    template_name = 'home.html'    

def PerfilView(request):
	usuario = CustomUser.objects.get(username=request.user)
	userdata = CompleteUser.objects.get(customuser_ptr_id=usuario.id)
	return render(request,'perfil.html',{'userdata':userdata},)
# Create your views here.
