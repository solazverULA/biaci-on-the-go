from django.urls import path

from . import views

urlpatterns = [
    path('', views.buscador, name='buscador_libro'),
    path('libros/', views.LibrosVista.as_view(), name='libros'),
    #path('buscador/libro', views.Inicio.as_view(), name='libro'),
    #path('buscador/libro/<cota>', views.Inicio.as_view(), name='ejemplar'),
]