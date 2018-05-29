from django import forms

from .models import Revista

from libro.models import Biblioteca


Options = (
        ('0', 'Titulo'),
        ('1', 'Serie'),
        ('2', 'Cota'),
     )


class ConsultaRevistaForm(forms.ModelForm):

    buscar_por = forms.ChoiceField(label='Buscar por', widget=forms.Select, choices=Options)
    biblioteca = forms.ModelChoiceField(
        label='Biblioteca',
        queryset=Biblioteca.objects.all(),
        required=False
    )

    class Meta:
        model = Revista
        fields = (
            'titulo',
        )

    def limpiar_palabra(self):

        data = self.cleaned_data['limpiar_palabra']

        return data
