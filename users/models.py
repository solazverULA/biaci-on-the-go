from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager 
from django.core.validators import RegexValidator
from datetime import datetime # Para fecha de Email
from django.urls import reverse  # Usado para generar URL en LogEmail


ESTADO_USUARIO = (
    ('Suspendido', 'Suspendido'),
    ('Bloqueado', 'Bloqueado'),
    ('Insolvente', 'Insolvente'),
    ('Solvente', 'Solvente'),
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
        primary_key=True,
        validators=[RegexValidator(regex="^[V|E]{1}[0]{1}[0-9]{7,9}$",message="Formato de Cedula invalido , ej: V0123456")],
        help_text='Fortamto: V012345678',
    )
	estado = models.CharField(
        max_length=15,
        choices=ESTADO_USUARIO,
        default='Solvente',
    )
	sexo = models.CharField(max_length=1, choices=SEXO)
	cod_area = models.CharField(max_length=4,
        validators=[RegexValidator(regex="^[0]{1}[2-4]{1}[1-9]{1}[1-9]{1}$",message="Codigo de Area invalido , ej: 0274")],
    )
	num_telefono = models.CharField(max_length=7)
	direccion = models.CharField(max_length=150)    


class RegistedUserId(models.Model):
    """"docstring for RegistedUser"""
    cedula = models.CharField(
		primary_key=True,
        max_length=11, 
        unique= True,
        validators=[RegexValidator(regex="^[V|E]{1}[0]{1}[0-9]{7,9}$",message="Formato de Cedula invalido , ej: V0123456")],
        help_text='Fortamto: V012345678',
    )


class LogCorreo(models.Model):
    """
    Modelo para los log del envio de correo
    :Example:
        Envio de correo de una reserva, notificacion,...
    """
    emisor = models.EmailField(max_length=254)
    receptor = models.CharField(max_length=100)
    estado = models.IntegerField()
    asunto = models.CharField(max_length=250)
    fecha = models.DateTimeField(default=datetime.now)

    def get_absolute_url(self):
        """
        Devuelve la url para acceder a un log de los correos
        """
        return reverse('detalle-log', args=[str(self.id)])
