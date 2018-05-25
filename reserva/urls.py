from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.ReservaLibros.as_view(), name='lista'),
    path('reservar/', views.Reservar, name='reservar'),
]