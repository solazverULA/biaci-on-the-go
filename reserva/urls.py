from django.urls import path

from . import views

urlpatterns = [
    path('', views.Reserva, name='reserva'),
    path('list/', views.ReservaLibros.as_view(), name='lista'),
]
