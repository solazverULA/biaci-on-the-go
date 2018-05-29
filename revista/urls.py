from django.urls import path

from . import views

urlpatterns = [
    path('', views.buscador, name='buscador_revista'),
    path('revistas/', views.RevistaVista.as_view(), name='revistas'),
    path('<pk>/revistas/', views.EjemplaresVista.as_view(), name='ejemplar_revista'),
]