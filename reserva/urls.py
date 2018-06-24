from django.urls import path

from . import views

urlpatterns = [

    path('list/', views.ErrorReserva.as_view(), name='error_reserva'),
    path('error/', views.ReservaLibros.as_view(), name='lista'),
    path('<int:id_ejemplar>', views.Reservar, name='reservar'),
    path('(?<id_reserva>\d+)$', views.Reserva_delete, name='eliminar'),
]
