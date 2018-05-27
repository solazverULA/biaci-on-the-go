from django.db import models
from datetime import datetime
from libro.models import Ejemplar
from users.models import CustomUser

# Create your models here.
class Prestamo(models.Model):
    id_usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True)
    id_ejemplar = models.ForeignKey(Ejemplar, on_delete=models.CASCADE,null=True)
    fecha_prestamo = models.DateTimeField(default=datetime.now())
    fecha_entrega = models.DateTimeField(default=datetime.now())
