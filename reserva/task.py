from __future__ import absolute_import, unicode_literals

from celery import shared_task, Celery, task

from time import sleep

from .models import Reserva, Ejemplar, HistorialReserva

from datetime import datetime, timezone, timedelta # Para obtener el tiempo actual

from users.models import LogCorreo # Modelo para log de correo, usado en envio cuando se reserva

from django.core.mail import send_mail # Para enviar correo de que reservaste un libro


app = Celery('biaci_go')

@task()
def vencer_reservas():
    """
    Esta funcion realiza la tarea de cambiar el estado de las reservas a Vencido en funcion de la fecha de caducidad y
    agrega actividad del historial.
    :return: Mensaje de Exito: Se marcaron reservas como vencidas
    """
    # Consulto reservas activas
    r_activa = Reserva.objects.filter(estado='A')
    if r_activa.exists() == True:
        for activa in r_activa.all():
            fecha_caducidad = activa.fecha_caducidad
            hoy = datetime.now(timezone.utc)
            # Si la fecha de caducidad es menor a la actual cambio estado a vencido
            if str(fecha_caducidad) < str(hoy):
                # Actualizo estado en reserva
                activa.estado = 'V'
                activa.save()

                # Guardo en historial
                reserva_fk = Reserva.objects.get(pk=activa.id) # Busco reserva desde id de for
                historial = HistorialReserva(id_reserva=reserva_fk, accion='V')
                historial.save()

                # Envio un correo al usuario que su reserva a expirado
                correo = send_mail('Reserva Vencida en BIACI on The Go',
                                   'Se ha vencido la reserva de su libro, pasado 2 dias para volver a reservar este mismo libro '
                                   'para buscar el libro.', 'biacionthego@gmail.com', [activa.id_usuario.email])
                if correo == True:
                    # Guardo en Log que el correo si se envio
                    env = LogCorreo(emisor='biacionthego@gmail.com', receptor=activa.id_usuario.email, estado='E',
                                    asunto='Reserva Vencida', fecha=datetime.now(timezone.utc))
                    env.save()
                else:
                    # Guardo en Logo que el correo por x razon no se envio
                    env = LogCorreo(emisor='biacionthego@gmail.com', receptor=activa.id_usuario.email, estado='R',
                                    asunto='Reserva Vencida', fecha=datetime.now(timezone.utc))
                    env.save()

    return 'Se marcaron reservas como vencidas'