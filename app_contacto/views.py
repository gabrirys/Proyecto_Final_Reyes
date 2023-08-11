from django.shortcuts import render, redirect
from django.urls import reverse
from app_contacto.models import Contacto
from app_contacto.forms import ContactoFormulario

def contactar(request):
   if request.method == "POST":
       formulario = ContactoFormulario(request.POST)
       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario
           nombre = data["nombre"]
           email = data["email"]
           telefono = data["telefono"]
           mensaje = data["mensaje"]
           
           contacto = Contacto(nombre=nombre, email=email, telefono=telefono, mensaje=mensaje)  # lo crean solo en RAM
           contacto.save()  # Lo guardan en la Base de datos

           # Redirecciono al usuario a la página inicio
           url_exitosa = reverse('inicio')  # me regresa a inicio
           return redirect(url_exitosa)
   else:  # GET
       formulario = ContactoFormulario()
   http_response = render(
       request=request,
       template_name='app_contacto/contacto.html',
       context={'formulario': formulario}
   )
   return http_response
