from django import forms
from .models import Reserva


class ReservaForm(forms.ModelForm):

    #id_ejemplar = forms.CharField()

    def __init__(self, *args, **kwargs):
        self.ejemplar = kwargs.pop('ejemplar', None)
        super(ReservaForm, self).__init__(*args, **kwargs)
        self.fields['fecha_reserva'].widget.attrs['readonly'] = True
        self.fields['fecha_caducidad'].widget.attrs['readonly'] = True
        self.fields['id_ejemplar'].initial=self.ejemplar
        self.fields['id_ejemplar'].widget = forms.HiddenInput()


    class Meta:
        model = Reserva
        fields = [
            'id_ejemplar',
            'fecha_reserva',
            'fecha_caducidad',
        ]

        labels = {
            'id_ejemplar':'Cota del ejemplar',
            'fecha_reserva':'Fecha de reserva',
            'fecha_caducidad':'Fecha de caducidad',
        }

        widgets = {
            'id_ejemplar':forms.TextInput(attrs = {'class':'form-control'}),
            'fecha_reserva':forms.TextInput(attrs = {'class':'form-control'}),
            'fecha_caducidad':forms.TextInput(attrs = {'class':'form-control'}),
        }
