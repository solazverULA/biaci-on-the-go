from django.template.response import TemplateResponse

from django.http import HttpResponseRedirect

from django.shortcuts import render, get_object_or_404

from django.views.generic import View


from .models import Libro

from tesis.models import Tesis

from revista.models import Revista

from reserva.models import Reserva


from .forms import ConsultaLibroForm

from consulta.models import Consulta


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

        # Verifico que no haya ningun ejemplar reservado y lo envio en la vista
        reserva = Reserva.objects.filter(id_ejemplar__libro__cota=pk)
        reservado = reserva.exists()

        # Falta agregarle al objeto el titulo y el autor
        # Verifico si el titulo no esta en las consultas para agregarlo si no esta 
        if Consulta.objects.filter(username=request.user, titulo=libro.titulo).exists() == False:
            for autor in libro.autor.all():
                autor
            busqueda = Consulta(username=request.user, titulo=libro.titulo, autor_nombre=autor.nombre, autor_apellido=autor.apellido, tipo_material="Libro")
            busqueda.save()
        
        return render(request, 'ejemplar.html', context={'ejemplar': libro, 'reservado': reservado,})


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


class ConsultaTodo(View):

    def post(self, request, *args, **kwargs):

        context = {
            'palabra': request.POST['palabra'],
            'libro': Libro.objects.filter(titulo__icontains=request.POST['palabra']),
            'tesis': Tesis.objects.filter(titulo__icontains=request.POST['palabra']),
            'revista': Revista.objects.filter(titulo__icontains=request.POST['palabra']),
        }

        return TemplateResponse(request, 'consulta.html', context)
