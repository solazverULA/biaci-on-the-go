from django import forms

from tesis.models import Tesis

from libro.models import Biblioteca


Options = (
        ('0', 'Titulo'),
        ('1', 'Autor'),
        ('2', 'Area'),
        ('3', 'Cota'),
     )


class ConsultaTesisForm(forms.ModelForm):

    buscar_por = forms.ChoiceField(label='Buscar por', widget=forms.Select, choices=Options)
    biblioteca = forms.ModelChoiceField(
        label='Biblioteca',
        queryset=Biblioteca.objects.all(),
        required=False
    )

    class Meta:
        model = Tesis
        fields = (
            'titulo',
        )

    def limpiar_palabra(self):

        data = self.cleaned_data['limpiar_palabra']

        return data
