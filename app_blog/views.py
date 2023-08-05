from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ArticuloFormulario


def crear_articulo(request):
    if request.method == "POST":
        formulario = ArticuloFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            url_exitosa = reverse('articulo_exitoso')
            return redirect(url_exitosa)
    else:  # GET
        formulario = ArticuloFormulario()
        http_response = render(
        request=request,
        template_name='crear_articulo.html',
        context={'formulario': formulario}
    )
    return http_response
            
