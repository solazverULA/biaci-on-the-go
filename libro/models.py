from django.db import models

from django.urls import reverse  # Usado para generar URL

import uuid

ESTADO_EJEMPLAR = (
    ('P', 'Prestado'),
    ('D', 'Disponible'),
    ('B', 'Bloqueado'),  # ejemplares de consulta interna
)


class Biblioteca(models.Model):
    """
    Modelo que representa un biblioteca de la ULA (ej. Biaci, Trujillo, etc).
    """
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    estado = models.CharField(max_length=80)
    cuidad = models.CharField(max_length=80)
    avenida = models.CharField(max_length=80)
    calle = models.CharField(max_length=80)
    edificio = models.CharField(max_length=80)

    def __str__(self):
        """
        Cadena para representar el objeto en Admin
        """
        return self.nombre


class Materia(models.Model):
    """
    Modelo que representa una materia
    """
    nombre = models.CharField(max_length=20)

    def __str__(self):
        """
        Cadena para representar el objeto en Admin
        """
        return self.nombre


class Idioma(models.Model):
    """
    Modelo que representa u lenguaje (ej. español, ingles, etc.)
    """
    nombre = models.CharField(max_length=50)

    def __str__(self):
        """
        Cadena que representa el modelo objeto
        """
        return self.nombre


class Autor(models.Model):
    """
    Representacion del modelo Autor.
    """
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)

    class Meta:
        """
        Clase para ordenar al momento de consultar
        """
        ordering = ["apellido", "nombre"]

    def get_absolute_url(self):
        """
        Retorna la url para ver detalles de autor.
        """
        return reverse('detalle-autor', args=[str(self.id)])

    def __str__(self):
        """
        Cadena para representar el objeto.
        """
        return '{0}, {1}'.format(self.apellido, self.nombre)


class Libro(models.Model):
    """
    Modelo que representa un libro (pero no un ejemplar para prestar).
    """
    cota = models.CharField(max_length=20, primary_key=True)
    titulo = models.CharField(max_length=200)
    anio = models.PositiveSmallIntegerField()
    idioma = models.CharField(max_length=15)
    lugar_publicacion = models.TextField(max_length=50)
    editorial = models.CharField(max_length=50)
    isbn = models.CharField('ISBN', max_length=13,
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    descripcion = models.TextField(max_length=1000)
    autor = models.ManyToManyField(Autor)
    materia = models.ManyToManyField(Materia)
    idioma = models.ForeignKey('Idioma', on_delete=models.SET_NULL, null=True)
    biblioteca = models.ForeignKey('Biblioteca', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """
        Cadena para representar el objeto
        """
        return self.titulo

    def get_absolute_url(self):
        """
        Devuelve la url para acceder a u registro de este libro
        """
        return reverse('ejemplar', args=[str(self.cota)])


class Ejemplar(models.Model):
    """
        Modelo que representa un ejemplar de un libro
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    libro = models.ForeignKey('Libro', on_delete=models.SET_NULL, null=True)
    estado = models.CharField(max_length=1, choices=ESTADO_EJEMPLAR, blank=True, default='D')

    def __str__(self):
        """
        Cadena para representar el objeto
        """
        return '{0} ({1})'.format(self.id, self.libro.titulo)
        # return f'{self.id} ({self.book.title})'

    def get_absolute_url(self):
        """
        Devuelve la url para acceder a un registro de este ejemplar
        """
        return reverse('detalle-ejemplar', args=[str(self.id)])