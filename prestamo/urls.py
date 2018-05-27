from django.urls import path
from . import views

urlpatterns = [
    path('prestamos/', views.PrestamosLista, name='lista_prestamos'),

]
