from django import forms
from .models import Reserva


class ReservaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        """
        Funcion para inicializar valores del formulario.
        :param args:
        :param kwargs: recibo el id del ejemplar.
        """
        self.ejemplar = kwargs.pop('ejemplar', None)
        super(ReservaForm, self).__init__(*args, **kwargs)
        self.fields['fecha_reserva'].widget.attrs['readonly'] = True
        self.fields['fecha_caducidad'].widget.attrs['readonly'] = True
        self.fields['id_ejemplar'].required = False
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
            'id_ejemplar':'Id del ejemplar',
            'fecha_reserva':'Fecha de reserva',
            'fecha_caducidad':'Fecha de caducidad',
        }

        widgets = {
            'id_ejemplar':forms.TextInput(attrs = {'class':'form-control'}),
            'fecha_reserva':forms.TextInput(attrs = {'class':'form-control'}),
            'fecha_caducidad':forms.TextInput(attrs = {'class':'form-control'}),
        }
