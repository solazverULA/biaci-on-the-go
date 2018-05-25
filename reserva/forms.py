from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):

    class Meta:
        model = Reserva

        fields = [
            'id_usuario',
            'id_ejemplar',
            'fecha_reserva',
            'fecha_caducidad',
        ]

        labels = {
            'id_usuario':'Usuario',
            'id_ejemplar':'Cota del ejemplar',
            'fecha_reserva':'Fecha de reserva',
            'fecha_caducidad':'Fecha de caducidad',
        }

        widgets = {
            'id_usuario':forms.Select(attrs = {'class':'form-control'}),
            'id_ejemplar':forms.Select(attrs = {'class':'form-control'}),
            'fecha_reserva':forms.TextInput(attrs = {'class':'form-control'}),
            'fecha_caducidad':forms.TextInput(attrs = {'class':'form-control'}),
        }
