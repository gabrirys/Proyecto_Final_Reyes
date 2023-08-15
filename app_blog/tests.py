from django.test import TestCase

from django.utils import timezone
from .models import Articulo
from django.contrib.auth.models import User


class ArticuloTest(TestCase):
# Creación del usuario y articulo para usar en los test
    def setUp(self):
        self.usuario = User.objects.create(username='testuser')
        self.articulo = Articulo.objects.create(
            titulo='Título de prueba',
            subtitulo='Subtítulo de prueba',
            contenido='Contenido de prueba',
            fecha_publicado=timezone.now(),
            autor=self.usuario
        )

# Comprobar si el str funciona correctamente
    def test_creacion_articulo(self):
        self.assertEqual(self.articulo.__str__(), 'Título de prueba - testuser -')
    
# Comproobamos si la fecha se establece automaticamente
    def test_fecha_publicado_al_crear(self):
        self.assertIsNotNone(self.articulo.fecha_publicado)
    
# Comprobamos si el método save actualiza correctamente
    def test_guardar_articulo(self):
        self.articulo.titulo = 'Titulo actualizado'
        self.articulo.save()
        self.assertEqual(Articulo.objects.get(pk=self.articulo.pk).titulo, 'Titulo actualizado')