from django.test import TestCase

from libro.models import Autor, Biblioteca, Libro, Idioma, Materia


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

    

class BibliotecaModeloTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        Biblioteca.objects.create(codigo = "euct", nombre = "Biblioteca Integrada de Arquitectura Ciencias e Ingenieria",
                                    estado = "Estado Bolivariano de Merida", ciudad = "Casigua del Cubo",
                                    avenida = "La Hechicera", calle =  "S/N",
                                    edificio = "C" )
    def test_codigo(self):
        biblioteca=Biblioteca.objects.get(codigo="euct")
        field_label = biblioteca._meta.get_field('codigo').verbose_name
        self.assertEquals(field_label, 'codigo')

    def test_codigo_max_caracteres(self):
        biblioteca=Biblioteca.objects.get(codigo="euct")
        max_length = biblioteca._meta.get_field('codigo').max_length
        self.assertEquals(max_length, 10)

    def test_nombre(self):
        biblioteca=Biblioteca.objects.get(codigo="euct")
        field_label = biblioteca._meta.get_field('nombre').verbose_name
        self.assertEquals(field_label, 'nombre')

    def test_nombre_max_caracteres(self):
        biblioteca=Biblioteca.objects.get(codigo="euct")
        max_length = biblioteca._meta.get_field('nombre').max_length
        self.assertEquals(max_length, 100)

    def test_estado(self):
        biblioteca=Biblioteca.objects.get(codigo="euct")
        field_label = biblioteca._meta.get_field('estado').verbose_name
        self.assertEquals(field_label, 'estado')

    def test_estado_max_caracteres(self):
        biblioteca=Biblioteca.objects.get(codigo="euct")
        max_length = biblioteca._meta.get_field('estado').max_length
        self.assertEquals(max_length, 80)

    def test_ciudad(self):
        biblioteca=Biblioteca.objects.get(codigo="euct")
        field_label = biblioteca._meta.get_field('ciudad').verbose_name
        self.assertEquals(field_label, 'ciudad')

    def test_ciudad_max_caracteres(self):
        biblioteca=Biblioteca.objects.get(codigo="euct")
        max_length = biblioteca._meta.get_field('ciudad').max_length
        self.assertEquals(max_length, 80)

    def test_avenida(self):
        biblioteca=Biblioteca.objects.get(codigo="euct")
        field_label = biblioteca._meta.get_field('avenida').verbose_name
        self.assertEquals(field_label, 'avenida')

    def test_avenida_max_caracteres(self):
        biblioteca=Biblioteca.objects.get(codigo="euct")
        max_length = biblioteca._meta.get_field('avenida').max_length
        self.assertEquals(max_length, 80)

    def test_calle(self):
        biblioteca=Biblioteca.objects.get(codigo="euct")
        field_label = biblioteca._meta.get_field('calle').verbose_name
        self.assertEquals(field_label, 'calle')

    def test_calle_max_caracteres(self):
        biblioteca=Biblioteca.objects.get(codigo="euct")
        max_length = biblioteca._meta.get_field('calle').max_length
        self.assertEquals(max_length, 80)

    def test_edificio(self):
        biblioteca=Biblioteca.objects.get(codigo="euct")
        field_label = biblioteca._meta.get_field('edificio').verbose_name
        self.assertEquals(field_label, 'edificio')

    def test_edificio_max_caracteres(self):
        biblioteca=Biblioteca.objects.get(codigo="euct")
        max_length = biblioteca._meta.get_field('edificio').max_length
        self.assertEquals(max_length, 80)

    def test_objecto_str_nombre(self):
        # mostrar el nombre de la biblioteca
        biblioteca=Biblioteca.objects.get(codigo="euct")
        nombre_esperado = '%s' % (biblioteca.nombre)
        self.assertEquals(nombre_esperado, str(biblioteca))


