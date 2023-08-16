from django.test import TestCase
from django.contrib.auth.models import User
from .models import Thread, Message

# TEST PARA:
# Crear hilos
# Asignarles usuarios
# Recuperar hilos a partir de sus usuarios
# Crear mensajes, asignarlos a hilos y recuperarlos


# Crear crear los usuarios y el hilo
class ThreadTestCase(TestCase):
    def setUp(self):
        self.u1 = User.objects.create_user('u1', None, '1234')
        self.u2 = User.objects.create_user('u2', None, '1234')
        
        self.thread = Thread.objects.create()
        self.thread.user.add(self.u1, self.u2)
    
    def test_add_user_to_thread(self): # Comprobar si el hilo tiene dos usuarios
        self.thread.user.add(self.u1, self.u2)
        self.assertEqual(len(self.thread.user.all()), 2) 
        
    def test_filter_threads_by_user(self): # Recuperar un hilo ya existente a partir de sus usuarios
        self.thread.user.add(self.u1, self.u2)
        threads = Thread.objects.filter(user=self.u1).filter(user=self.u2)
        self.assertEqual(self.thread, threads[0])
        
        
