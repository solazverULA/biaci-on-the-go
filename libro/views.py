from django.template.response import TemplateResponse

from django.shortcuts import render

from django.views.generic import View

from .models import Libro, Autor, Materia, Ejemplar, Biblioteca, Idioma


def buscador(request):

    biblioteca = Biblioteca.objects.all()

    return render(

        request,
        'buscar.html',
        context={'biblioteca':biblioteca},

    )


class LibrosVista(View):

    def post(self, request, *args, **kwargs):
        
        context = {
            'libro': Libro.objects.filter(titulo__icontains=request.POST['palabra']),
            'palabra': request.POST['palabra']
        }

        return TemplateResponse(request, 'libros.html', context)