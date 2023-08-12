from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from .models import Articulo
from .forms import ArticuloFormulario
from django.contrib.auth.mixins import LoginRequiredMixin
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


class ArticuloCreateView(LoginRequiredMixin, CreateView):
    model = Articulo
    form_class = ArticuloFormulario
    template_name = 'app_blog/articulo_formulario.html'
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.autor = self.request.user  # Asignar el autor al usuario actual
        self.object.save()
        return redirect(reverse('articulo_detail', args=[self.object.pk]))


class ArticuloUpdateView(LoginRequiredMixin, UpdateView):
    model = Articulo
    form_class = ArticuloFormulario
    template_name = 'articulo_formulario.html'
    context_object_name = 'articulo'
    success_url = reverse_lazy('articulo_lista')


class ArticuloDeleteView(LoginRequiredMixin, DeleteView):
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
            
