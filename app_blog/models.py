from django.db import models
from django.contrib.auth.models import User

class Articulo(models.Model):
    titulo = models.CharField(max_length=128)
    subtitulo = models.CharField(max_length=128)
    contenido = models.TextField(blank=True)
    fecha_publicado = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articulos_creados', null=True)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True) # imagen
    
    
    def __str__(self):
        return f"{self.titulo} - {self.autor} -" 