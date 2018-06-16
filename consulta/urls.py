from django.urls import path
from libro.views import EjemplaresVista

from . import views

urlpatterns = [
    path('sugerencias/', views.ConsultaList.as_view(), name='sugerencias'),
    path('<pk>/libros/', EjemplaresVista.as_view(), name='ejemplar'),
]
