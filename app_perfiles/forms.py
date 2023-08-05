from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm): # CREACION DE USUARIO
   # Esto es un ModelForm
   password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
   password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

   class Meta:
       model = User
       fields = ['nombre', 'apellido', 'usuario', 'email', 'password1', 'password2']
       
       
       
class UserUpdateForm(forms.ModelForm): # EDIDCIÓN DE USUARIO
    
    class Meta:
       model = User
       fields = ['nombre', 'apellido', 'email']