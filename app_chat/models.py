from django.db import models

from django.contrib.auth.models import User

class Message(models.Model): # Mensaje
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created']
        
class Thread(models.Model): # Hilo
    user = models.ManyToManyField(User, related_name='threads')
    message = models.ManyToManyField(Message)