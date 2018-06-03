from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.views.generic import View, CreateView
from .models import Reserva, Ejemplar
from .forms import ReservaForm

# Create your views here.


class ReservaLibros(View):
    def get(self, request, *args, **kwargs):
        context = {
            'reserva': Reserva.objects.filter(id_usuario=request.user),
            }
        return TemplateResponse(request, 'lista_reserva.html', context)


def Reservar(request, id_ejemplar):

    """
    def get_form_kwargs(self):
        kwargs = super(Reservar, self).get_form_kwargs()

        # La variable que queremos pasar al formulario
        kwargs.update({'ejemplar': self.id_ejemplar})

        return kwargs
    """
    if request.method == 'POST':
        tap = Reserva(id_usuario=request.user)
        form = ReservaForm(request.POST, request.FILES, instance=tap)
        if form.is_valid():
            form.save(),
            return redirect ('lista')
    else:
        form = ReservaForm()
        return render(request,'reservar.html',{'form':form, 'ejemplar':id_ejemplar})


def Reserva_delete(request,id_reserva):
    reserva = Reserva.objects.get(id=id_reserva)
    reserva.delete()
    return redirect('lista')
