from django.template.response import TemplateResponse

from django.http import HttpResponseRedirect

from django.shortcuts import render, get_object_or_404

from django.views.generic import View


from .models import Libro, Autor, Materia, Ejemplar, Biblioteca, Idioma


from .forms import ConsultaLibroForm


def buscador(request):

    """form = ConsultaLibroForm()

    return render(

        request,
        'buscar.html',
        context={'form': form},

    )"""
    if request.method == 'POST':

        form = ConsultaLibroForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = ConsultaLibroForm()

    return render(request, 'buscar.html', {'form': form})


class LibrosVista(View):

    def post(self, request, *args, **kwargs):

        palabra = request.POST['titulo']

        biblioteca = request.POST['biblioteca']
        por = request.POST['buscar_por']

        if por == '0' and biblioteca == '':
            consulta = Libro.objects.filter(titulo__icontains=palabra)

        if por == '1' and biblioteca == '':
            consulta = Libro.objects.filter(autor__icontains=palabra)

        if por == '2' and biblioteca == '':
            consulta = Libro.objects.filter(isbn__icontains=palabra)

        if por == '3' and biblioteca == '':
            consulta = Libro.objects.filter(cota__icontains=palabra)

        if por == '0' and biblioteca != '':
            consulta = Libro.objects.filter(titulo__icontains=palabra, biblioteca=biblioteca)

        if por == '1' and biblioteca != '':
            consulta = Libro.objects.filter(autor__icontains=palabra, biblioteca=biblioteca)

        if por == '2' and biblioteca != '':
            consulta = Libro.objects.filter(isbn__icontains=palabra, biblioteca=biblioteca)

        if por == '3' and biblioteca != '':
            consulta = Libro.objects.filter(cota__icontains=palabra, biblioteca=biblioteca)

        get_object_or_404(consulta, pk=1)

        return TemplateResponse(request, 'libros.html', {'consulta': consulta, 'palabra':palabra})


class EjemplaresVista(View):

    def get(self, request, pk, **kwargs):

        try:
            libro = Libro.objects.get(pk=pk)
        except Libro.DoesNotExist:
            raise Http404("El libro no existe")

        # book_id=get_object_or_404(Book, pk=pk)

        return render(
            request,
            'ejemplar.html',
            context={'ejemplar': libro, }
        )
    """def ejemplar(request, pk):
        try:
            libro_id = Libro.objects.get(pk=pk)
        except Libro.DoesNotExist:
            raise Http404("Este Libro no existe")

        # book_id=get_object_or_404(Book, pk=pk)

        return render(
            request,
            'ejemplar.html',
            context={'ejemplar': libro_id, }
        )
    """