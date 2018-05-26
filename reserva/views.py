from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.views.generic import View, CreateView
from .models import Reserva
from .forms import ReservaForm

# Create your views here.

class ReservaLibros(View):
    def get(self, request, *args, **kwargs):
        context = {
            'reserva': Reserva.objects.all(),
            }
        return TemplateResponse(request, 'lista_reserva.html', context)

def Reservar(request):
    if request.method == 'POST':
        tap = Reserva(id_usuario=request.user)
        form = ReservaForm(request.POST,request.FILES, instance=tap)
        if form.is_valid():
            form.save(),
            return redirect ('lista')
    else:
       form = ReservaForm()
       return render(request,'reservar.html',{'form':form})

def Reserva_delete(request,id_reserva):
    reserva = Reserva.objects.get(id=id_reserva)
    reserva.delete()
    return redirect('lista')
