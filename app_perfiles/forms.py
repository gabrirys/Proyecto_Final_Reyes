from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Avatar


class UserRegisterForm(UserCreationForm): # CREACION DE USUARIO

   password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
   password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

   class Meta:
       model = User
       fields = ['last_name', 'first_name', 'username', 'email', 'password1', 'password2']
            
       
class UserUpdateForm(forms.ModelForm): # EDIDCIÓN DE USUARIO
    
    class Meta:
       model = User
       fields = ['last_name', 'first_name', 'email']
       

class AvatarFormulario(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ['imagen']