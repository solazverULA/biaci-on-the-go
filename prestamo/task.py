from __future__ import absolute_import, unicode_literals

from celery import shared_task, Celery, task

from time import sleep

from .models import Prestamo

from datetime import datetime, timezone, timedelta # Para obtener el tiempo actual

from users.models import LogCorreo # Modelo para log de correo, usado en envio cuando se reserva

from django.core.mail import send_mail # Para enviar correo de que reservaste un libro


app = Celery('biaci_go')

@task(name='enviar_notificacion')
def enviar_notificacion():
    """
    Esta funcion realiza en funcion de los prestamos del usuario el envio de la notificacion
    agrega actividad  del correo en el log.
    :return: Mensaje de Exito: Se notifico al cliente que debe entregar el libro
    """
    # Consulto prestamos que no se han vencido
    hoy = datetime.now(timezone.utc)
    prestamos = Prestamo.objects.filter(fecha_entrega__lte=hoy)
    if prestamos.exists() == True:
        for prestamo in prestamos.all():
            # Obtengo fechas de 3 dias antes para enviar la notificacion
            dias = timedelta(days=3)
            fecha_empieza = prestamo.fecha_entrega - dias
            if str(hoy) >= str(fecha_empieza) and str(hoy) <= str(prestamo.fecha_entrega):

                # Envio un correo al usuario de que ha reservado el libro tal
                correo = send_mail('Recordatorio de BIACI on The Go',
                                   'Usted debe entregar un libro en la biblioteca entreguelo antes de o estara '
                                   'insolvente', 'biacionthego@gmail.com', [prestamo.id_usuario.email])
                if correo == True:
                    # Guardo en Log que el correo si se envio
                    env = LogCorreo(emisor='biacionthego@gmail.com', receptor=prestamo.id_usuario.email, estado='E',
                                    asunto='Envio de Notificacion', fecha=datetime.now(timezone.utc))
                    env.save()
                else:
                    # Guardo en Logo que el correo por x razon no se envio
                    env = LogCorreo(emisor='biacionthego@gmail.com', receptor=prestamo.id_usuario.email, estado='R',
                                    asunto='Envio de Notificacion', fecha=datetime.now(timezone.utc))
                    env.save()

                # Salio Bien liste las reservas del usuario, incluyendo la que se hizo

                return 'Se notifico al usuario que debe entregar el libro'
    else:
        return 'No se notifico al usuario que debe entregar el libro'


