from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager 


ESTADO_USUARIO = (
    ('S', 'Suspendido'),
    ('B', 'Bloqueado'),
    ('I', 'Insolvente'),
    ('T', 'Solvente'),
)

SEXO = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
)

class CustomUserManager(UserManager):
    pass

class CustomUser(AbstractUser):
	objects = CustomUserManager()

class CompleteUser(CustomUser):
	cedula = models.CharField(max_length=15, unique= True)
	estado = models.CharField(
        max_length=1,
        choices=ESTADO_USUARIO,
        default='T',
    )
	sexo = models.CharField(max_length=1, choices=SEXO)
	cod_area = models.CharField(max_length=4)
	num_telefono = models.CharField(max_length=8)
	direccion = models.TextField(max_length=150)
	carrera = models.CharField(max_length=100, blank=True)
    
    
# Create your models here.
