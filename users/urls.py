# users/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('users/signup/', views.SignUp.as_view(), name='signup'),
    path('', views.HomePageView, name='home'),
    path('', views.Sugerencias, name='sugerencias'),
    path('perfil/', views.PerfilView, name='perfil'),
    path('users/signup/error/', views.ErrorSignUp.as_view(), name='error_signup'),

]
