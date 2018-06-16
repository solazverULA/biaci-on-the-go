from django.db import models

from libro.models import Idioma, Biblioteca, Materia

from django.urls import reverse  # Usado para generar URL

from django.core.validators import RegexValidator

ESTADO_EJEMPLAR = (
    ('P', 'Prestado'),
    ('D', 'Disponible'),
    ('B', 'Bloqueado'),  # ejemplares de consulta interna
    ('R', 'Reservado'),
)


class Revista(models.Model):
    """
    Modelo que representa una revista (pero no un ejemplar para prestar).
    """
    cota = models.CharField(max_length=20, primary_key=True)
    titulo = models.CharField(max_length=150)
    anio = models.PositiveSmallIntegerField()
    idioma = models.ForeignKey(Idioma, on_delete=models.SET_NULL, null=True)
    lugar_publicacion = models.TextField(max_length=50)
    descripcion = models.TextField(max_length=1000)
    numero = models.CharField(max_length=30)
    serie = models.CharField(max_length=30)
    biblioteca = models.ForeignKey(Biblioteca, on_delete=models.SET_NULL, null=True)
    area = models.CharField(max_length=30)


    def __str__(self):
        """
        Cadena para representar el objeto
        """
        return self.cota

    def get_absolute_url(self):
        """
        Devuelve la url para acceder a un registro de esta revista
        """
        return reverse('ejemplar_revista', args=[str(self.cota)])
        #return "/revista/%i/" % self.cota


class EjemplarRevista(models.Model):
    """
        Modelo que representa un ejemplar de una revista
    """
    ejemplar = models.CharField(
        max_length=4,
        validators=[RegexValidator(regex="^[e]{1}[0-9]{1,3}$", message="Formato de ejemplar incorrecto, ej: e1")],
    )
    revista = models.ForeignKey('Revista', on_delete=models.SET_NULL, null=True)
    estado = models.CharField(max_length=1, choices=ESTADO_EJEMPLAR, blank=True, default='D')

    def __str__(self):
        """
        Cadena para representar el objeto
        """
        return '{0} ({1})'.format(self.revista.cota, self.ejemplar)
        # return f'{self.id} ({self.book.title})'

    class Meta:
        """
        Simulacion de clave compuesta con campo unico tipo tupla
        """
        unique_together = (("ejemplar", "revista"),)

    def get_absolute_url(self):
        """
        Devuelve la url para acceder a un registro de este ejemplar
        """
        return reverse('detalle-ejemplar-revista', args=[str(self.id)])
