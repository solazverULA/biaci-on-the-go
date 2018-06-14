from django.template.response import TemplateResponse

from django.http import HttpResponseRedirect

from django.shortcuts import render, get_object_or_404

from django.views.generic import View

from .models import Tesis

from .forms import ConsultaTesisForm

from consulta.models import Consulta

def buscador(request):

    if request.method == 'POST':

        form = ConsultaTesisForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = ConsultaTesisForm()

    return render(request, 'buscar_tesis.html', {'form': form})


class TesisVista(View):

    def post(self, request, *args, **kwargs):

        palabra = request.POST['titulo']

        biblioteca = request.POST['biblioteca']
        por = request.POST['buscar_por']

        if por == '0' and biblioteca == '':
            consulta = Tesis.objects.filter(titulo__icontains=palabra)

        if por == '1' and biblioteca == '':
            consulta = Tesis.objects.filter(autor__nombre__icontains=palabra)

        if por == '2' and biblioteca == '':
            consulta = Tesis.objects.filter(area__icontains=palabra)

        if por == '3' and biblioteca == '':
            consulta = Tesis.objects.filter(cota__icontains=palabra)

        if por == '0' and biblioteca != '':
            consulta = Tesis.objects.filter(titulo__icontains=palabra, biblioteca=biblioteca)

        if por == '1' and biblioteca != '':
            consulta = Tesis.objects.filter(autor__nombre__icontains=palabra, biblioteca=biblioteca)

        if por == '2' and biblioteca != '':
            consulta = Tesis.objects.filter(area__icontains=palabra, biblioteca=biblioteca)

        if por == '3' and biblioteca != '':
            consulta = Tesis.objects.filter(cota__icontains=palabra, biblioteca=biblioteca)

        return TemplateResponse(request, 'tesis.html', {'consulta': consulta, 'palabra':palabra})


class EjemplaresTesis(View):

    def get(self, request, pk, **kwargs):

        try:
            tesis = Tesis.objects.get(pk=pk)
        except Tesis.DoesNotExist:
            raise Http404("La tesis no existe")
        # Falta agregarle al objeto el titulo y el autor
        # Verifico si el titulo no esta en las consultas para agregarlo si no esta 
        if Consulta.objects.filter(username=request.user, titulo=tesis.titulo).exists() == False:
            for autor in tesis.autor.all():
                autor
            busqueda = Consulta(username=request.user,cota=tesis.cota,titulo=tesis.titulo,autor_nombre=autor.nombre,autor_apellido=autor.apellido,tipo_material="Tesis")
            busqueda.save()
        
        return render(request,'ejemplar_tesis.html',context={'ejemplar': tesis, })
