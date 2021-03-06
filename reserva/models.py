from django.db import models

from datetime import datetime, timedelta

from libro.models import Ejemplar, Libro

from users.models import CustomUser

from django.urls import reverse  # Usado para generar URL


ESTADO_RESERVA = (
    ('A', 'Activo'),
    ('V', 'Vencido'),
    ('E', 'Eliminado'),
)


class Reserva(models.Model):
    """
    Modelo que representa la reserva de un libro existente en la biblioteca
    """
    fecha_reserva = models.DateTimeField(default=datetime.now)
    fecha_caducidad = models.DateTimeField(default=datetime.now()+timedelta(hours=10))
    id_ejemplar = models.ForeignKey(Ejemplar, on_delete=models.CASCADE, null=True)
    id_usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    estado = models.CharField(max_length=1, choices=ESTADO_RESERVA, blank=True, default='A')

    def get_absolute_url(self):
        """
        Devuelve la url para acceder a un registro de esta reserva
        """
        return reverse('reserva', args=[str(self.id)])


class HistorialReserva(models.Model):
    """
    Modelo que representa el historial de reverva
    """
    id_reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE, null=True)
    accion = models.CharField(max_length=1, choices=ESTADO_RESERVA, blank=True, default='A')
    fecha = models.DateTimeField(default=datetime.now)

    class Meta:
        """
        Clase para ordenar al momento de consultar
        """
        ordering = ["id", "fecha"]

    def get_absolute_url(self):
        """
        Devuelve la url para acceder a un registro de esta reserva
        """
        return reverse('historial_reserva', args=[str(self.id)])
