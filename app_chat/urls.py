from django.urls import path
from .views import (mensajes_privados, DetailMs)

urlpatterns = [
    path('chat/<str:username>', mensajes_privados, name='mensajes_privados'),
    path('chat/<str:username>', DetailMs.as_view(), name='detailms'),
]