from django.urls import path

from . import views

urlpatterns = [
    path('', views.buscador, name='buscador_libro'),
    path('libros/', views.LibrosVista.as_view(), name='libros'),
    #path('buscador/libro', views.Inicio.as_view(), name='libro'),
    path('libros/<pk>', views.EjemplaresVista.as_view(), name='ejemplar'),
]