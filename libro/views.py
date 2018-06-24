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


class LibrosVista(View):

    """
    Esta clase recibe los parametros del formulario `ConsultaLibroForm`
    """
    def post(self, request, *args, **kwargs):

        """
         La funcion proviene de la clase `LibrosVista`

         Se comparan los distintos parametros recibidos por el post para realizar la consulta.

         :type arg3: No se esta usando
         :type arg4: No se esta usando
         :return: Retorna vista `libros.html`
         :rtype: TemplateResponse
        """

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


def buscador(request):

    """
    Funcion para mostrar un libro en la data

    A partir de los datos de la consulta, se listan los libros disponibles, dependiendo de lo retornado en el formulario.

    :param func: Funcion buscador
    :type func: Llamada
    :param args: Argumento a procesar
    :type args: Request
    :returns: Una render a la plantilla `buscar.html`
    :rtype: Render

    .. note:: Se utilizan datos del formulario `ConsultaLibroForm`
    """
    if request.method == 'POST':

        form = ConsultaLibroForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = ConsultaLibroForm()

    return render(request, 'buscar.html', {'form': form})


class EjemplaresVista(View):
    """
    Esta clase lista los ejemplares disponibles de un libro, previa llamada de la clase `LibrosVista`
    """

    def get(self, request, pk, **kwargs):
        """
        Funcion para recopilar la informacion de los ejemplares del libro seleccionado

        A partir de los datos de la consulta, se listan los ejemplares disponibles, dependiendo de lo retornado en el formulario.

        :type arg3: Cota (Definido en el modelo)
        :returns: Una render a la plantilla `ejemplar.html`
        :rtype: Render

        """
        try:
            libro = Libro.objects.get(pk=pk)
        except Libro.DoesNotExist:
            raise Http404("El libro no existe")

        # Verifico que no haya ningun ejemplar reservado y lo envio en la vista
        reserva = Reserva.objects.filter(id_ejemplar__libro__cota=pk, estado='A')
        reservado = reserva.exists()


        # Falta agregarle al objeto el titulo y el autor
        # Verifico si el titulo no esta en las consultas para agregarlo si no esta
        if Consulta.objects.filter(username=request.user, titulo=libro.titulo).exists() == False:
            for autor in libro.autor.all():
                autor
            busqueda = Consulta(username=request.user, cota=libro.cota, titulo=libro.titulo, autor_nombre=autor.nombre, autor_apellido=autor.apellido, tipo_material="Libro")
            busqueda.save()

        return render(request, 'ejemplar.html', context={'ejemplar': libro, 'reservado': reservado})


class ConsultaTodo(View):
    """
    Esta clase lista todo los libros, revista y tesis disponibles en el OPAC.

    .. note:: La busqueda solo se realiza al usar el buscador del menu.
    """
    def post(self, request, *args, **kwargs):

        # Se verifica si se devuelven consultas vacias
        libro_exist = Libro.objects.filter(titulo__icontains=request.POST['palabra']).exists()
        tesis_exist = Tesis.objects.filter(titulo__icontains=request.POST['palabra']).exists()
        revista_exist = Revista.objects.filter(titulo__icontains=request.POST['palabra']).exists()

        # Comparo resultados de los query y declaro variable para trabajar en el template
        if libro_exist == False and tesis_exist == False and revista_exist == False:
            query_vacia = True
        else:
            query_vacia = False

        context = {
            'query': query_vacia,
            'palabra': request.POST['palabra'],
            'libro': Libro.objects.filter(titulo__icontains=request.POST['palabra']),
            'tesis': Tesis.objects.filter(titulo__icontains=request.POST['palabra']),
            'revista': Revista.objects.filter(titulo__icontains=request.POST['palabra']),
        }

        return TemplateResponse(request, 'consulta.html', context)
