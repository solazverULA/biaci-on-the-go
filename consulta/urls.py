from django.urls import path

from . import views

urlpatterns = [
    path('sugerencias/', views.ConsultaList.as_view(), name='sugerencias'),
]
