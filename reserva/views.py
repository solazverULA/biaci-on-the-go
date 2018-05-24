from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.views.generic import View
from .models import Reserva
from .forms import ReservaForm

# Create your views here.
class ReservaLibros(View):
    def get(self, request, *args, **kwargs):
        context = {
            #'reserva': Reserva.objects.all(),
            }
        return TemplateResponse(request, 'lista_reserva.html', context)

def Reserva(request):
    return render(request,'reserva.html')

def Reservar(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('reservar')
