from django.db import models

from libro.models import Autor

from libro.models import Idioma

from libro.models import Biblioteca

from django.urls import reverse  # Usado para generar URL

from django.core.validators import RegexValidator

ESTADO_EJEMPLAR = (
    ('P', 'Prestado'),
    ('D', 'Disponible'),
    ('B', 'Bloqueado'),  # ejemplares de consulta interna
)


class Tesis(models.Model):
    """
    Modelo que representa una tesis (pero no un ejemplar para prestar).
    """
    cota = models.CharField(max_length=20, primary_key=True)
    titulo = models.CharField(max_length=150)
    anio = models.PositiveSmallIntegerField()
    idioma = models.ForeignKey(Idioma, on_delete=models.SET_NULL, null=True)
    lugar_publicacion = models.TextField(max_length=50)
    descripcion = models.TextField(max_length=1000)
    autor = models.ManyToManyField(Autor)
    area = models.CharField(max_length=30)
    estado = models.CharField(max_length=1, choices=ESTADO_EJEMPLAR, blank=True, default='D')
    biblioteca = models.ForeignKey(Biblioteca, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        """
        Cadena para representar el objeto
        """
        return self.cota

    def get_absolute_url(self):
        """
        Devuelve la url para acceder a u registro de esta revista
        """
        return reverse('ejemplar_tesis', args=[str(self.cota)])
