from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    contenido = RichTextField()
    fecha_publicado = models.DateTimeField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articulos_creados', null=True)
    imagen = models.ImageField(upload_to='images_blog/', null=True, blank=True) # imagen
    
    def __str__(self):
        return f"{self.titulo} - {self.autor} -" 
        
    def save(self, *args, **kwargs):
        if not self.id:  # Si es un nuevo artículo
            self.fecha_publicado = timezone.now()  # Establecer la fecha actual al crear
        super().save(*args, **kwargs)