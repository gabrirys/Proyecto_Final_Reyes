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
        self.u3 = User.objects.create_user('u3', None, '1234')
        
        self.thread = Thread.objects.create()
        self.thread.user.add(self.u1, self.u2)
    
    
    def test_add_user_to_thread(self): # Comprobar si el hilo tiene dos usuarios
        self.thread.user.add(self.u1, self.u2)
        self.assertEqual(len(self.thread.user.all()), 2) 
        
        
    def test_filter_threads_by_user(self): # Recuperar un hilo ya existente a partir de sus usuarios
        self.thread.user.add(self.u1, self.u2)
        threads = Thread.objects.filter(user=self.u1).filter(user=self.u2)
        self.assertEqual(self.thread, threads[0])
        
        
    def test_add_message_to_thread(self): # Crear mensajes
        self.thread.user.add(self.u1, self.u2)
        msg1 = Message.objects.create(user= self.u1, content= "Como va")
        msg2 = Message.objects.create(user= self.u2, content= "Todo viento")
        self.thread.message.add(msg1, msg2)
        self.assertEqual(len(self.thread.message.all()), 2)
        
        
    def test_add_message_from_user_not_in_thread(self):
        self.thread.user.add(self.u1, self.u2)
        msg1 = Message.objects.create(user= self.u1, content= "Como va")
        msg2 = Message.objects.create(user= self.u2, content= "Todo viento")
        msg3 = Message.objects.create(user= self.u3, content= "El espía")
        self.thread.message.add(msg1, msg2, msg3)
        self.assertEqual(len(self.thread.message.all()), 2)
        
        
    def test_find_thread_with_custom_manager(self):
        self.thread.user.add(self.u1, self.u2)
        thread = Thread.objects.find(self.u1, self.u2)
        self.assertEqual(self.thread, thread)
        thread = Thread.objects.find(self.u1, self.u3)
        self.assertEqual(None, thread)
        
    
    def test_find_or_create_thread_with_custom_manager(self):
        self.thread.user.add(self.u1, self.u2)
        thread = Thread.objects.find_or_create(self.u1, self.u2)
        self.assertEqual(self.thread, thread)
        thread = Thread.objects.find_or_create(self.u1, self.u3)
        self.assertIsNotNone(thread)
        
        