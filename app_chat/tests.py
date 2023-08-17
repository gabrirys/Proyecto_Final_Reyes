from django.test import TestCase
from .models import CanalMensaje, CanalUsuario, Canal
from django.contrib.auth import get_user_model

User = get_user_model()

class CanalTestCase(TestCase):
    def setUp(self):
        self.usuario_a = User.objects.create(username='usuario1' ,password='')
        self.usuario_b = User.objects.create(username='usuario2' ,password='')
        self.usuario_c = User.objects.create(username='usuario3' ,password='')