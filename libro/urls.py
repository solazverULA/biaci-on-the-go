from django.urls import path

from . import views

urlpatterns = [
    path('', views.buscador, name='buscador_libro'),
    path('libros/', views.LibrosVista.as_view(), name='libros'),
    #path('libros/', views.LibrosVista, name='libro'),
    path('<pk>/libros/', views.EjemplaresVista.as_view(), name='ejemplar'),
]