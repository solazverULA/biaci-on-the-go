from django.urls import path

from . import views

urlpatterns = [

    path('error/', views.ErrorReserva.as_view(), name='error_reserva'),
    path('list/', views.ReservaLibros.as_view(), name='lista'),
    path('<int:id_ejemplar>', views.Reservar, name='reservar'),
    path('(?<id_reserva>\d+)$', views.Reserva_delete, name='eliminar'),
]
