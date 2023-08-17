from django.urls import path
from .views import (mensajes_privados)

urlpatterns = [
    path('chat/<str:username>', mensajes_privados, name='mensajes_privados')
]