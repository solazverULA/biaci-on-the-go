# biaci-go

## Versiones
    - Python 3.6.3
    - psycopg2-2.7.4
    - Django-2.0.5
    - virtualenv-15.2.0
    - pip3
    - psql (PostgreSQL) 9.6.8

## Poner por defecto temporalmente python 3
    ~$ alias python=python3
    ~$ python --version

## Trabajar con Entorno Virtual
    ~$ virtualenv ~/.virtualenvs/biblio_app --python=python3
    ~$ source ~/.virtualenvs/biblio_app/bin/activate

## Crear en Postgre Base de datos (Modificar usuario en settings.py)
    ~$ CREATE DATABASE biaci_go

## Migrar cambios a Postgre
    ~$ python manage.py migrate

## Correr Servidor Django
    ~$ python manage.py runserver

## Migrar modelos de app
    ~$ python manage.py makemigrations biaci_go

## Crear Superusuario para Admin
    ~$ python manage.py createsuperuser

## Para desplegar en heroku
    https://tutorial-extensions.djangogirls.org/es/heroku/
    http://pythonpiura.org/posts/2016/04/17/deployando-proyectos-django-en-heroku/

## Solo para Administrador heroku
    ~$ git push heroku master
    ~$ heroku run python manage.py migrate
    ~$ heroku ps:scale web=1

## Correr migraciones
    ~$ python manage.py makemigrations

## Aplicar migraciones en base de datos
    ~$ python manage.py migrate

## Abrir Shell de Django
  ~$ python manage.py shell
