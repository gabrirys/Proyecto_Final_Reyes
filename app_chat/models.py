from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed


class ThreadManager(models.Manager):
    def find(self, user1, user2):
        querySet = self.filter(user=user1).filter(user=user2)
        if len(querySet) > 0:
            return querySet[0]
        return None
        
    def find_or_create(self, user1, user2):
        thread = self.find(user1, user2)
        if thread is None:
            thread = Thread.objects.create()
            thread.user.add(user1, user2)
        return thread
        
        
class Message(models.Model): # Mensaje
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created']
        
class Thread(models.Model): # Hilo
    user = models.ManyToManyField(User, related_name='threads')
    message = models.ManyToManyField(Message)
    objects = ThreadManager()
    
    
def messages_changed(sender, **kwargs):
    instance = kwargs.pop("instance", None)
    action = kwargs.pop("action", None)
    pk_set = kwargs.pop("pk_set", None)
    
    false_pk_set = set() # Conjunto que almacena los mensajes fraudulentos
    
    if action is "pre_add":
        for msg_pk in pk_set:
            msg = Message.objects.get(pk=msg_pk)
            if msg.user not in instance.user.all():
                print("Ups...({}) no forma parte del hilo".format(msg.user))
                false_pk_set.add(msg_pk)
        
        pk_set.difference_update(false_pk_set)
    
    
m2m_changed.connect(messages_changed, sender=Thread.message.through)


    
    