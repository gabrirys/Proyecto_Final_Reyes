from django.test import TestCase
from django.contrib.auth.models import User
from .models import Chat, Message
from django.urls import reverse

class ChatTests(TestCase):
# Crear dos usarios para utilizar en el test
    def setUp(self):
        self.usuario_1 = User.objects.create_user(username='usuario1', password='password123')
        self.usuario_2 = User.objects.create_user(username='usuario2', password='password456')
        self.chat = Chat.objects.create(usuario_1=self.usuario_1, usuario_2=self.usuario_2)
    
# Comprobar la creración de mensajes
    def test_creacion_mensaje(self):
        mensaje = Message.objects.create(chat=self.chat, texto='Hola, usuario 2!')
        self.assertEqual(mensaje.chat, self.chat)
        self.assertEqual(mensaje.texto, 'Hola, usuario 2!')
  
# Comprobar el dialogo entre usuarios
    def test_dialogo_entre_usuarios(self):
        mensaje_1 = Message.objects.create(chat=self.chat, texto='Hola, usuario 2!')
        mensaje_2 = Message.objects.create(chat=self.chat, texto='Hola, usuario 1!')
        self.assertEqual(self.chat.message_set.count(), 2)
        self.assertIn(mensaje_1, self.chat.message_set.all())
        self.assertIn(mensaje_2, self.chat.message_set.all())
