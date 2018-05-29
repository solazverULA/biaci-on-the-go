from django.db import models
from datetime import datetime, timedelta
from libro.models import Ejemplar
from users.models import CustomUser

# Create your models here.


class Reserva(models.Model):
    fecha_reserva = models.DateTimeField(default=datetime.now)
    fecha_caducidad = models.DateTimeField(default=datetime.now()+timedelta(hours=10))
    id_ejemplar = models.ForeignKey(Ejemplar, on_delete=models.CASCADE,null=True)
    id_usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True)

    """
    def __unicode__(self):
        return self.id_usuario
    """

    def __str__(self):
        """
        Cadena para representar el objeto
        """
        return self.id

    def get_absolute_url(self):
        """
        Devuelve la url para acceder a u registro de esta reserva
        """
        return reverse('reserva', args=[str(self.id)])
