from __future__ import absolute_import, unicode_literals

from celery import shared_task, Celery, task

from .models import RegistedUserId

import csv # Para leer csv

import urllib, os, urllib.request # Para descargar archivo

from urllib.parse import urlparse


app = Celery('biaci_go')

import os.path

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@task()
def importar_usuarios():
    """
    Esta funcion carga la data de un archivo cvs, que se descarga localmente y se lee.
    :return: Mensaje de Exito: se cargo la data correctamente
    """
    # Consulto prestamos que no se han vencido
    #ruta = 'http://190.168.28.128/librum/anexos/14/09/17/QA261S34.csv'
    #filename = urlparse(ruta).path.split('/')[-1]
    #urllib.request.urlretrieve(ruta, os.path.join('static/data/', filename))

    with open(BASE_DIR+'/static/data/usuarios.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            persona = RegistedUserId.objects.filter(cedula=row['cedula'])
            if persona.exists() == False:
                p = RegistedUserId(cedula=row['cedula'])
                p.save()

    return ('Se leyo data nueva')