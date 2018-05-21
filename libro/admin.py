from django.contrib import admin

from .models import Libro, Autor, Materia, Ejemplar, Biblioteca, Idioma


admin.site.register(Libro)
admin.site.register(Autor)
admin.site.register(Materia)
admin.site.register(Ejemplar)
admin.site.register(Biblioteca)
admin.site.register(Idioma)

