from django.shortcuts import render, redirect

from django.template.response import TemplateResponse

from django.views.generic import View, CreateView

from datetime import datetime, timezone, timedelta # Para obtener el tiempo actual

from .models import Reserva, Ejemplar, HistorialReserva

from users.models import LogCorreo # Modelo para log de correo, usado en envio cuando se reserva

from .forms import ReservaForm

from django.core.mail import send_mail # Para enviar correo de que reservaste un libro

from prestamo.task import enviar_notificacion


class ReservaLibros(View):

    """
    Esta clase verifica las reservas realizadas por el usuario
    """

    def get(self, request, *args, **kwargs):
        """
            Funcion para recopilar la informacion de los ejemplares ejemplares reservado por el usuario logueado

            A partir de los datos de la consulta, se listan los datos de la reserva

            :returns: Una plantilla llamada `lista_reserva.html`
            :rtype: Template Response

        """
        if request.user.is_authenticated:
            context = {
                'reserva': Reserva.objects.filter(id_usuario=request.user, estado='A'),
                # Se agrega para saber si existen reservas del usuario, si no mostrar otro mensaje
                'query': Reserva.objects.filter(id_usuario=request.user, estado='A').exists(),
            }
            return TemplateResponse(request, 'lista_reserva.html', context)
            enviar_notificacion.delay()
        else:
            return redirect('login')


class ErrorReserva(View):

    """
    Esta clase muestra un error si la reserva no se pudo realizar
    """

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return TemplateResponse(request, 'error_reserva.html')
        else:
            return redirect('login')


def Reservar(request, id_ejemplar):

    """
    Funcion para reservar un ejemplar.

    0- Verifica que el mismo ejemplar no haya sido reservado en los ultimos dos dias por el mismo usuario
    1- Reserva el ejemplar.
    2. Guarda la reserva en un historial.
    3. Cambia el estado del ejemplar de disponible a reservado.

    :type args2: id del ejemplar a reservar
    :returns: un render a `reservar.html`
    :rtype: render

    """
    if request.method == 'POST':
        tap = Reserva(id_usuario=request.user)
        form = ReservaForm(request.POST, request.FILES, instance=tap)

        if form.is_valid():

            # Verificar si existe una reserva hecha por el mismo usuario y el mismo ejemplar recientemente 2Dias
            historial = HistorialReserva.objects.filter(id_reserva__id_ejemplar=id_ejemplar, id_reserva__id_usuario=request.user).order_by('-fecha')[:1]
            if historial.exists() == True:
                for h_reserva in historial.all():
                    fecha = h_reserva.fecha
                    hoy = datetime.now(timezone.utc)
                    dias = timedelta(days=2)
                    hoy_menos_dias = hoy - dias
                    if str(fecha) < str(hoy_menos_dias):
                        # Guardar reserva desde formulario
                        reserva_hecha = form.save()

                        # Guardar reserva en el historial como Activa
                        reserva_fk = Reserva.objects.get(pk=reserva_hecha.id)  # Busco reserva desde reserva guardada con form.save()
                        historial = HistorialReserva(id_reserva=reserva_fk, accion='A')
                        historial.save()

                        # Cambiar de estado del ejemplar que se reservo
                        ej = Ejemplar.objects.get(pk=id_ejemplar)
                        ej.estado = 'R'
                        ej.save()

                        # Envio un correo al usuario de que ha reservado el libro tal
                        correo = send_mail('Reserva en BIACI on The Go',
                                           'Usted ha reservado un libro en BIACI, tiene 10 horas '
                                           'para buscar el libro.', 'biacionthego@gmail.com', [request.user.email])
                        if correo == True:
                            # Guardo en Log que el correo si se envio
                            env = LogCorreo(emisor='biacionthego@gmail.com', receptor=request.user.email, estado='E',
                                            asunto='Reserva', fecha=datetime.now(timezone.utc))
                            env.save()
                        else:
                            # Guardo en Logo que el correo por x razon no se envio
                            env = LogCorreo(emisor='biacionthego@gmail.com', receptor=request.user.email, estado='R',
                                            asunto='Reserva', fecha=datetime.now(timezone.utc))
                            env.save()

                        # Salio Bien liste las reservas del usuario, incluyendo la que se hizo
                        return redirect('lista')
                    else:
                        # Si no se puede reservar porque hay una accion cercana con ese ejemplar envie error
                        return redirect('error_reserva')
            # Si no hay ningun movimiento de este ejemplar con este mismo usuario, reservo sin rollo
            else:
                # Guardar reserva desde formulario
                reserva_hecha = form.save()

                # Guardar reserva en el historial como Activa
                reserva_fk = Reserva.objects.get(
                    pk=reserva_hecha.id)  # Busco reserva desde reserva guardada con form.save()
                historial = HistorialReserva(id_reserva=reserva_fk, accion='A')
                historial.save()

                # Cambiar de estado del ejemplar que se reservo
                ej = Ejemplar.objects.get(pk=id_ejemplar)
                ej.estado = 'R'
                ej.save()

                # Envio un correo al usuario de que ha reservado el libro tal
                correo = send_mail('Reserva en BIACI on The Go', 'Usted ha reservado un libro en BIACI, tiene 10 horas '
                                                                 'para buscar el libro.', 'biacionthego@gmail.com', [request.user.email])
                if correo == True:
                    # Guardo en Log que el correo si se envio
                    env = LogCorreo(emisor='biacionthego@gmail.com', receptor=request.user.email, estado='E',
                                    asunto='Reserva', fecha=datetime.now(timezone.utc))
                    env.save()
                else:
                    # Guardo en Logo que el correo por x razon no se envio
                    env = LogCorreo(emisor='biacionthego@gmail.com', receptor=request.user.email, estado='R',
                                    asunto='Reserva', fecha=datetime.now(timezone.utc))
                    env.save()

                # Salio Bien listo las reservas del usuario, incluyendo la que se hizo
                return redirect('lista')
    else:
        form = ReservaForm(ejemplar=id_ejemplar)
        # Envio el numero del ejemplar hacia el formulario para que lo tome para la inserccion
        ej = Ejemplar.objects.get(pk=id_ejemplar)
        return render(request, 'reservar.html', {'form': form, 'ejemplar': ej})


def Reserva_delete(request, id_reserva):

    # Pongo mi reserva como eliminada
    reserva = Reserva.objects.get(id=id_reserva)
    reserva.estado='E'
    id_ejemplar = reserva.id_ejemplar.id
    reserva.save()

    # Guardo la eliminacion de mi reserva en el historial
    reserva_fk = Reserva.objects.get(pk=id_reserva)
    historial = HistorialReserva(id_reserva=reserva_fk, accion='E')
    historial.save()

    # Cambiar de estado del ejemplar que se reservo
    ej = Ejemplar.objects.get(pk=id_ejemplar)
    ej.estado = 'D'
    ej.save()

    # Envio un correo al usuario de que se ha eliminado la reserva el libro tal
    correo = send_mail('Eliminacion de Reserva en BIACI on The Go', 'Usted ha elimino la reserva solicitada.', 'biacionthego@gmail.com',
                       [request.user.email])
    if correo == True:
        # Guardo en Log que el correo si se envio
        env = LogCorreo(emisor='biacionthego@gmail.com', receptor=request.user.email, estado='E',
                        asunto='Eliminacion de Reserva', fecha=datetime.now(timezone.utc))
        env.save()
    else:
        # Guardo en Log que el correo por x razon no se envio
        env = LogCorreo(emisor='biacionthego@gmail.com', receptor=request.user.email, estado='R',
                        asunto='Eliminacion de Reserva', fecha=datetime.now(timezone.utc))
        env.save()

    return redirect('lista')
