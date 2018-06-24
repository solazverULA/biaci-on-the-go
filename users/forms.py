# users/forms.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from .models import CompleteUser


class CustomUserCreationForm(UserCreationForm):
	
	class Meta(UserCreationForm.Meta):
		model = CompleteUser
		fields = (
			'username',
			'first_name',
			'last_name',
			'cedula',
			'email',
			'cod_area' ,
			'num_telefono' ,
			'sexo' ,        
			'direccion',
		)
		
		labels = dict(username='Nombre de usuario', first_name='Nombre',
			last_name='Apellidos', email='Correo',sexo='Género',
			cedula='Cedula de Identidad',cod_area='Codigo de area',num_telefono='Numero de telefono',direccion='Direccion')

		

class CustomUserChangeForm(UserChangeForm):
	class Meta:
		model = CompleteUser
		fields = UserChangeForm.Meta.fields