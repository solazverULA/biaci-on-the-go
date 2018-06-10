# users/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('users/signup/', views.SignUp.as_view(), name='signup'),
    path('', views.HomePageView.as_view(), name='home'),
    path('perfil/', views.PerfilView, name='perfil'),
    
]
