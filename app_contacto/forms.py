from django import forms


class ContactoFormulario(forms.Form):
    nombre = forms.CharField(label='Nombre', required=True, max_length=128)
    email = forms.EmailField(label='Correo Electrónico', required=True)
    telefono = forms.CharField(label='Télefono', max_length=20)
    mensaje = forms.CharField(label='Mensaje', required=True, widget=forms.Textarea)