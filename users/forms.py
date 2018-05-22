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
	        'sexo' ,        
	        'direccion',
        )


class CustomUserChangeForm(UserChangeForm):
	class Meta:
		model = CompleteUser
		fields = UserChangeForm.Meta.fields