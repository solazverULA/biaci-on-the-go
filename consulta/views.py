from django.shortcuts import render, redirect
from .models import Consulta
from django.views.generic import View
from django.template.response import TemplateResponse

# Create your views here.
class ConsultaList(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            context = {
                # Ultimas 20 consultas ordenadas por orden descendente de acuerdo a la fecha #
                'consulta': Consulta.objects.filter(username=request.user).order_by('-fecha')[:20],
                }
            return TemplateResponse(request, 'lista_consultas.html', context)
        else:
            return redirect('login')

# FALTA
#class Sugerencias(View):
#    def get(self, request, *args, **kwargs):
