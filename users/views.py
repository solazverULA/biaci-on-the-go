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
    userdata = CompleteUser.objects.filter(first_name="Manuel")
    #userdata = CompleteUser.objects.CustomUser.filter(first_name=request.user)
    #userdata = CompleteUser.objects.all().filter(user = request.user)
    return render(request,'perfil.html',{'userdata':userdata})
# Create your views here.
