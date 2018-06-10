from django.test import TestCase

from libro.models import Autor


class AutorModeloTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Configurar objetos no modificados utilizados por todos los métodos del test
        Autor.objects.create(nombre='Rodolfo', apellido='Sumoza')

    def test_nombre(self):
        autor=Autor.objects.get(id=1)
        field_label = autor._meta.get_field('nombre').verbose_name
        self.assertEquals(field_label, 'nombre')

    def test_nombre_max_caracteres(self):
        autor=Autor.objects.get(id=1)
        max_length = autor._meta.get_field('nombre').max_length
        self.assertEquals(max_length, 20)

    def test_apellido(self):
        autor=Autor.objects.get(id=1)
        field_label = autor._meta.get_field('apellido').verbose_name
        self.assertEquals(field_label, 'apellido')

    def test_apellido_max_caracteres(self):
        autor=Autor.objects.get(id=1)
        max_length = autor._meta.get_field('apellido').max_length
        self.assertEquals(max_length, 20)

    def test_objecto_apellido_nombre_separados_por_coma(self):
        # Al mostrar los autores los expreso como Sumoza, Rodolfo
        autor=Autor.objects.get(id=1)
        expected_object_name = '%s, %s' % (autor.apellido, autor.nombre)
        self.assertEquals(expected_object_name, str(autor))

    def test_get_absolute_url(self):
        autor=Autor.objects.get(id=1)
        # Prueba la ruta absoluta, tambien fall si no la cree
        self.assertEquals(autor.get_absolute_url(),'/libro/autor/1')