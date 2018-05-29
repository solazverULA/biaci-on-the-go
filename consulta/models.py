from django.db import models

# Create your models here.
class Consulta(models.Model):
    username = models.CharField(max_length=20)
    titulo = models.CharField(max_length=150)
    autor_nombre = models.CharField(max_length=20)
    autor_apellido = models.CharField(max_length=20)
    tipo_material = models.CharField(max_length=20)
