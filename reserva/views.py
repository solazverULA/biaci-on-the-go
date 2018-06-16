from django.shortcuts import render, redirect

from django.template.response import TemplateResponse

from django.views.generic import View, CreateView

from .models import Reserva, Ejemplar, EjemplarRevista

from .forms import ReservaForm


class ReservaLibros(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            context = {
                'reserva': Reserva.objects.filter(id_usuario=request.user),
                # Se agrega para saber si existen reservas del usuario, si no mostrar otro mensaje
                'reserva_vacia': Reserva.objects.filter(id_usuario=request.user).exists(),
            }
            return TemplateResponse(request, 'lista_reserva.html', context)
        else:
            return redirect('login')


def Reservar(request, id_ejemplar, tipo_material):

    if request.method == 'POST':
        tap = Reserva(id_usuario=request.user)
        form = ReservaForm(request.POST, request.FILES, instance=tap)
        if form.is_valid():
            form.save()
            # Cambiar de estado del ejemplar que se reservo
            if tipo_material == 1:
                # Si es libro #
                ej = Ejemplar.objects.get(pk=id_ejemplar)
            if tipo_material == 2:
                # Si es revista #
                ej = EjemplarRevista.objects.get(pk=id_ejemplar)
            ej.estado = 'R'
            ej.save()
            return redirect('lista')
    else:
        form = ReservaForm(ejemplar=id_ejemplar, tipo=tipo_material)
        if tipo_material == 1:
            ej = Ejemplar.objects.get(pk=id_ejemplar)
        if tipo_material == 2:
            ej = EjemplarRevista.objects.get(pk=id_ejemplar)
        return render(request, 'reservar.html', {'form': form, 'ejemplar': ej})

def Reserva_delete(request, id_reserva):

    reserva = Reserva.objects.get(id=id_reserva)
    reserva.delete()
    return redirect('lista')
