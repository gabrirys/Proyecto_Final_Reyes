from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mail # para que envíe un mail con la info del contacto
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
           
           #(Envío de correo electrónico
            # subject = 'Nuevo mensaje de contacto'
            # message = f'Nombre: {nombre}\nEmail: {email}\nTeléfono: {telefono}\nMensaje: {mensaje}'
            # from_email = 'tu@email.com'
            # to_email = ['destinatario@email.com']
            # send_mail(subject, message, from_email, to_email, fail_silently=False)

           # Redirecciono a una página con mensaje de éxito
            url_exitosa = reverse('contacto_exitoso')
            return redirect(url_exitosa)
           
    else:  # GET
        formulario = ContactoFormulario()
        http_response = render(
        request=request,
        template_name='app_contacto/contacto.html',
        context={'formulario': formulario}
    )
    return http_response

def contacto_exitoso(request):
    return render(request, 'app_contacto/contacto_exitoso.html')