from django.urls import path

from . import views

urlpatterns = [
    path('', views.buscador, name='buscador_tesis'),
    path('tesis/', views.TesisVista.as_view(), name='tesis'),
    path('<pk>/tesis/', views.EjemplaresTesis.as_view(), name='ejemplar_tesis'),
]