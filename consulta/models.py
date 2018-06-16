from django.db import models

from datetime import datetime

from django.urls import reverse  # Usado para generar URL


class Consulta(models.Model):

    """
    Clase que define las consultas hechas por un usuario
    """
    username = models.CharField(max_length=20)
    cota = models.CharField(max_length=150)
    titulo = models.CharField(max_length=150)
    autor_nombre = models.CharField(max_length=20)
    autor_apellido = models.CharField(max_length=20)
    tipo_material = models.CharField(max_length=20)
    fecha = models.DateTimeField(default=datetime.now)

    def __str__(self):
        """
        Cadena para representar el objeto
        """
        return self.cota

    def get_absolute_url(self):
        """
        Devuelve la url para acceder a un registro de esta consulta
        """
        return reverse('ejemplar', args=[str(self.cota)])
