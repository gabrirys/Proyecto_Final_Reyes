from django.urls import path
from .views import (ChatListView, ChatDetailView, MessageCreateView)


urlpatterns = [
    path('', ChatListView.as_view(), name='chat_list'),
    path('chat/<int:pk>/', ChatDetailView.as_view(), name= 'chat_detail'),
    path('crear-mensaje/<int:chat_id>/', MessageCreateView.as_view(), name='crear_mensaje'),
]

  