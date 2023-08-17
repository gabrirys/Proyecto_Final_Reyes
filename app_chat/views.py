from typing import Any, Optional
from django.db import models
from django.shortcuts import render
from .models import CanalMensaje, CanalUsuario, Canal
from django.http import HttpResponse, Http404

from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class CanalDetailView(LoginRequiredMixin, DetailView):
	template_name= 'app_chat/canal_detail.html'
	queryset = Canal.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)

		obj = context['object']
		print(obj)

		context['si_canal_miembro'] = self.request.user in obj.usuarios.all()

		return context


class DetailMs(LoginRequiredMixin, DetailView):

    template_name = 'app_chat/canal_detail.html'
    
    def get_object(self, *args, **kwargs):
        username = self.kwargs.get("username")
        mi_username = self.request.user.username
        canal, _ = Canal.objects.obtener_o_crear_canal_ms(mi_username, username)
        
        if username == mi_username:
            mi_canal, _ = Canal.objects.obtener_o_crear_canal_usuario_actual(self.request.user)

        return mi_canal
        
        if canal == None:
            raise Http404
        
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
    



