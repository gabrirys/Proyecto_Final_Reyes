from django import forms
from .models import Articulo
from ckeditor.widgets import CKEditorWidget


class ArticuloFormulario(forms.ModelForm):
    contenido = forms.CharField(widget=CKEditorWidget())  # Agrega CKEditorWidget al campo de contenido
    class Meta:
        model = Articulo
        fields = ['titulo', 'subtitulo', 'contenido', 'imagen', 'pie_imagen']