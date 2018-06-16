# Biaci On The Go (https://biacionthego.herokuapp.com/)

## Crear y activar Entorno Virtual
    ~$ virtualenv ~/.virtualenvs/biblio_app --python=python3
    ~$ source ~/.virtualenvs/biblio_app/bin/activate

## Instalar versiones de los requerimientos
    - Python 3.6.3
    - pip3
    - psycopg2-2.7.4
    - Django-2.0.5
    - virtualenv-15.2.0
    - psql (PostgreSQL) 9.6.8
    - Dj-databse-url 0.5.0
    - Gunicorn 19.8.1
    - Pillow 5.1.0
    - Selenium 1.11.0
    - Sphinx 1.7.5

## Poner por defecto temporalmente python 3
    ~$ alias python=python3
    ~$ python --version

## Crear en Postgre Base de datos (Modificar usuario en settings.py)
    ~$ CREATE DATABASE biaci_db

## Migrar modelos
    ~$ python manage.py makemigrations

## Migrar cambios a Postgre
    ~$ python manage.py migrate

## Correr Servidor Django
    ~$ python manage.py runserver

## Crear Superusuario para Admin
    ~$ python manage.py createsuperuser

## Para desplegar en heroku (solo administrador Heroku)
    http://pythonpiura.org/posts/2016/04/17/deployando-proyectos-django-en-heroku/
    ~$ git push heroku master
    ~$ heroku run python manage.py migrate
    ~$ heroku ps:scale web=1
    ~$ DEBUG = False

## Para generar documentacion
    ~$ make html
    ~$ make latexpdf (teniendo instalado latex y latexmk)
