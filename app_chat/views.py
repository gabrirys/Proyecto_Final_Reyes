from typing import Any, Optional
from django.db import models
from django.shortcuts import render
from .models import CanalMensaje, CanalUsuario, Canal
from django.http import HttpResponse

from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class DetailMs(LoginRequiredMixin, DetailView):
    
    def get_object(self, *args, **kwargs):
        username = self.kwargs.get("username")
        mi_username = self.request.user.username
        canal, _ = Canal.objects.obtener_o_crear_canal_ms(mi_username, username)
        
        return canal
        



def mensajes_privados(request, username, *args, **kwargs):
    
    if not request.user.is_authenticated:
        return HttpResponse("Prohibido")
      
    mi_username = request.user.username
    
    canal, created = Canal.objects.obtener_o_crear_canal_ms(mi_username, username)
  
    if created:
        print("Si, creado")
        
    Usuarios_canal = canal.canalusuario_set.all().values("usuario__username")
    
    return HttpResponse(f"Nuestro Canal - {canal.count()}")
    



