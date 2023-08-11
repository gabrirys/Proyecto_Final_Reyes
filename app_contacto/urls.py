from django.urls import path
from .views import contactar

urlpatterns = [
    path('contacto/', contactar, name='contactar'),
]