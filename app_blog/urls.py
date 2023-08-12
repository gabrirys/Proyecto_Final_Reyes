from django.urls import path
from .views import (
    ArticuloListView,
    ArticuloDetailView,
    ArticuloCreateView,
    ArticuloUpdateView,
    ArticuloDeleteView
)

urlpatterns = [
    path('', ArticuloListView.as_view(), name='articulo_lista'),
    path('page<int:pk>/', ArticuloDetailView.as_view(), name='articulo_detail'),
    path('crear-articulo/', ArticuloCreateView.as_view(), name='articulo_crear'),
    path('editar-articulo/<int:pk>/', ArticuloUpdateView.as_view(), name='articulo_editar'),
    path('eliminar-articulo/<int:pk>/', ArticuloDeleteView.as_view(), name='articulo_eliminar'),
]