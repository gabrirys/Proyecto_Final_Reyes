from django import forms
from .models import Articulo


class ArticuloFormulario(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo', 'subtitulo', 'contenido', 'imagen']