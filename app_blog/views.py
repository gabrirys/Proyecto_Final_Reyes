from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from .models import Articulo
from .forms import ArticuloFormulario
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# CRUD (Vistas basadas en clases)

class ArticuloListView(ListView):
    model = Articulo
    template_name = 'articulo_lista.html'
    context_object_name = 'articulos'

class ArticuloDetailView(DetailView):
    model = Articulo
    template_name = 'app_blog/articulo_detail.html'
    context_object_name = 'articulo'

class ArticuloCreateView(CreateView):
    model = Articulo
    form_class = ArticuloFormulario
    template_name = 'app_blog/articulo_formulario.html'
    success_url = reverse_lazy('articulo_detail')

class ArticuloUpdateView(UpdateView):
    model = Articulo
    form_class = ArticuloFormulario
    template_name = 'articulo_formulario.html'
    context_object_name = 'articulo'
    success_url = reverse_lazy('articulo_lista')

class ArticuloDeleteView(DeleteView):
    model = Articulo
    template_name = 'articulo_confirm_delete.html'
    context_object_name = 'articulo'
    success_url = reverse_lazy('articulo_lista')



# CREAR ARTICULO BASADO EN FUNCIONES
# def crear_articulo(request):
#     if request.method == "POST":
#         formulario = ArticuloFormulario(request.POST, request.FILES)
#         if formulario.is_valid():
#             formulario.save()
#             url_exitosa = reverse('articulo_exitoso')
#             return redirect(url_exitosa)
#     else:  # GET
#         formulario = ArticuloFormulario()
#         http_response = render(
#         request=request,
#         template_name='articulo_crear.html',
#         context={'formulario': formulario}
#     )
#     return http_response
            
