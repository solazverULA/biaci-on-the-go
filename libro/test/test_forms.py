from django.test import TestCase
from libro.models import Biblioteca

# Create your tests here.

from libro.forms import ConsultaLibroForm 

class ConsultaLibroFormTest(TestCase):

    def test_Libro_form_buscarpor_label(self):
        form = ConsultaLibroForm()        
        self.assertTrue(form.fields['buscar_por'].label == None or form.fields['buscar_por'].label == 'Buscar por')

    def test_Libro_form_biblioteca_label(self):
        form = ConsultaLibroForm()  
        self.assertTrue(form.fields['biblioteca'].label == None or form.fields['biblioteca'].label ==  'Biblioteca')