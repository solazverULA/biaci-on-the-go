from django.template.response import TemplateResponse

from django.http import HttpResponseRedirect

from django.shortcuts import render, get_object_or_404

from django.views.generic import View

from .models import Revista

from .forms import ConsultaRevistaForm


def buscador(request):

    if request.method == 'POST':

        form = ConsultaRevistaForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = ConsultaRevistaForm()

    return render(request, 'buscar.html', {'form': form})

"""
class LibrosVista(View):

    def post(self, request, *args, **kwargs):

        palabra = request.POST['titulo']

        biblioteca = request.POST['biblioteca']
        por = request.POST['buscar_por']

        if por == '0' and biblioteca == '':
            consulta = Libro.objects.filter(titulo__icontains=palabra)

        if por == '1' and biblioteca == '':
            consulta = Libro.objects.filter(autor__nombre__icontains=palabra)

        if por == '2' and biblioteca == '':
            consulta = Libro.objects.filter(isbn__icontains=palabra)

        if por == '3' and biblioteca == '':
            consulta = Libro.objects.filter(cota__icontains=palabra)

        if por == '0' and biblioteca != '':
            consulta = Libro.objects.filter(titulo__icontains=palabra, biblioteca=biblioteca)

        if por == '1' and biblioteca != '':
            consulta = Libro.objects.filter(autor__nombre__icontains=palabra, biblioteca=biblioteca)

        if por == '2' and biblioteca != '':
            consulta = Libro.objects.filter(isbn__icontains=palabra, biblioteca=biblioteca)

        if por == '3' and biblioteca != '':
            consulta = Libro.objects.filter(cota__icontains=palabra, biblioteca=biblioteca)


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
    def ejemplar(request, pk):
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