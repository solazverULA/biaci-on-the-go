from django.shortcuts import render
from .models import Consulta
from django.views.generic import View
from django.template.response import TemplateResponse

# Create your views here.
class ConsultaList(View):
    def get(self, request, *args, **kwargs):
        context = {
            'consulta': Consulta.objects.filter(username=request.user),
            }
        return TemplateResponse(request, 'lista_consultas.html', context)
