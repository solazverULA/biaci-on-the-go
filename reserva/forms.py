from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):

    #id_ejemplar = forms.CharField()

    def __init__(self, *args, **kwargs):
        self.ejemplar = kwargs.pop('ejemplar', None)
        self.tipo = kwargs.pop('tipo', None)
        super(ReservaForm, self).__init__(*args, **kwargs)
        self.fields['fecha_reserva'].widget.attrs['readonly'] = True
        self.fields['fecha_caducidad'].widget.attrs['readonly'] = True
        self.fields['id_ejemplar'].required = False
        self.fields['id_ejemplar_revista'].required = False
        if self.tipo == 1:
            self.fields['id_ejemplar'].initial=self.ejemplar
            self.fields['id_ejemplar'].widget = forms.HiddenInput()
            self.fields['id_ejemplar_revista'].widget = forms.HiddenInput()
        if self.tipo == 2:
            self.fields['id_ejemplar_revista'].initial=self.ejemplar
            self.fields['id_ejemplar_revista'].widget = forms.HiddenInput()
            self.fields['id_ejemplar'].widget = forms.HiddenInput()

    class Meta:
        model = Reserva
        fields = [
            'id_ejemplar',
            'id_ejemplar_revista',
            'fecha_reserva',
            'fecha_caducidad',
        ]

        labels = {
            'id_ejemplar':'Cota del ejemplar',
            'id_ejemplar_revista':'Cota del ejemplar',
            'fecha_reserva':'Fecha de reserva',
            'fecha_caducidad':'Fecha de caducidad',
        }

        widgets = {
            'id_ejemplar':forms.TextInput(attrs = {'class':'form-control'}),
            'id_ejemplar_revista':forms.TextInput(attrs = {'class':'form-control'}),
            'fecha_reserva':forms.TextInput(attrs = {'class':'form-control'}),
            'fecha_caducidad':forms.TextInput(attrs = {'class':'form-control'}),
        }
