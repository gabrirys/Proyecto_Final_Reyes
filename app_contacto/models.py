from django.db import models

class Contacto(models.Model):
    nombre = models.CharField(max_length=128)
    email = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True)
    mensaje = models.TextField()

    def __str__(self):
        return f"{self.nombre}"
