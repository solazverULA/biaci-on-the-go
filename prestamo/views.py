from django.shortcuts import render
from django.template.response import TemplateResponse
from .models import Prestamo

# Create your views here.
def PrestamosLista(request):
    if request.method == 'GET':
        context = {
            'prestamo': Prestamo.objects.filter(id_usuario=request.user),
            }
        return TemplateResponse(request, 'lista_prestamos.html', context)
