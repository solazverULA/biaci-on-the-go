from django import forms

from .models import Libro, Biblioteca

Options = (
        ('0', 'Titulo'),
        ('1', 'Autor'),
        ('2', 'ISBN'),
        ('3', 'Cota'),
     )


class ConsultaLibroForm(forms.ModelForm):

    buscar_por = forms.ChoiceField(label='Buscar por', widget=forms.Select, choices=Options)
    biblioteca = forms.ModelChoiceField(
        label='Biblioteca',
        queryset=Biblioteca.objects.all(),
        required=False
    )

    class Meta:
        model = Libro
        fields = (
            'titulo',
        )

    def limpiar_palabra(self):

        data = self.cleaned_data['limpiar_palabra']

        return data
