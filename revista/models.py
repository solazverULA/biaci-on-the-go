from django.db import models

from libro.models import Idioma, Biblioteca, Materia

from django.urls import reverse  # Usado para generar URL

from django.core.validators import RegexValidator

ESTADO_EJEMPLAR = (
    ('B', 'Bloqueado'),  # ejemplares de consulta interna
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
    url = models.URLField()

    upload_path = 'images/portada'
    file_save_dir = '/images/portada/'

    # Campos para portada de libro
    imagen = models.ImageField(upload_to=upload_path, default='/images/portada/default.png')
    imagen_url = models.URLField()

    def save(self, *args, **kwargs):
        """
        Funcion que descargar la portada del libro pasada por el url y lo guarda localmente

        :param args: Parametro Vacio
        :param kwargs: Parametro Vacio
        :return: una funcion de guardar.
        """
        if self.imagen_url:
            import urllib, os, urllib.request
            from urllib.parse import urlparse
            filename = urlparse(self.imagen_url).path.split('/')[-1]
            # Guarda la imagen localmente despues de descargarla
            urllib.request.urlretrieve(self.imagen_url, os.path.join('static/images/portada/', filename))
            # Le guarda la ruta en el modelo donde esta la imagen local
            self.imagen = os.path.join(self.upload_path, os.path.join(self.file_save_dir, filename))
            super(Revista, self).save()

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
    estado = models.CharField(max_length=1, choices=ESTADO_EJEMPLAR, blank=True, default='B')

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
