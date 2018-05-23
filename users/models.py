from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager 
from django.core.validators import RegexValidator


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
	cedula = models.CharField(
        max_length=11, 
        unique= True,
        validators=[RegexValidator(regex="^[V|E]{1}[0]{1}[0-9]{7,9}$",message="Formato de Cedula invalido , ej: V0123456")],
    )
	estado = models.CharField(
        max_length=1,
        choices=ESTADO_USUARIO,
        default='T',
    )
	sexo = models.CharField(max_length=1, choices=SEXO)
	cod_area = models.CharField(max_length=4,
        validators=[RegexValidator(regex="^[0]{1}[2-4]{1}[1-9]{1}[1-9]{1}$",message="Codigo de Area invalido , ej: 0274")],
    )
	num_telefono = models.CharField(max_length=7)
	direccion = models.CharField(max_length=150)
	carrera = models.CharField(max_length=100, blank=True)
    
    
# Create your models here.
'''validators=[RegexValidator
                                      (regex="^[0-9]{10}$",
message="Invalid format for CI")]'''
