from django.shortcuts import render
from .models import CanalMensaje, CanalUsuario, Canal
from django.http import HttpResponse


def mensajes_privados(request, username, *args, **kwargs):
    
    if not request.user.is_authenticated:
        return HttpResponse("Prohibido")
      
    mi_username = request.user.username  
      
    canal_obj, created = Canal.objects.all().solo_dos().filtrar_username(mi_username).filtrar_username(username)
    if created:
        print("Si, creado")
        
    Usuarios_canal = canal_obj.canalusuario_set.all().values("usuario__username")
    
    return HttpResponse(f"Nuestro Canal - {canal_obj.count()}")
    



