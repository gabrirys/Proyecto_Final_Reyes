from django.urls import path
from .views import contactar, contacto_exitoso

urlpatterns = [
    path('', contactar, name='contactar'),
    path('contacto-exitoso/', contacto_exitoso, name='contacto_exitoso'),  
]