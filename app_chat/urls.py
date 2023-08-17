from django.urls import path
from .views import ThreadListView, ThreadDetailView



app_chat_patterns = ([
    path('', ThreadListView.as_view(), name='list'),
    path('thread/<int:pk>/', ThreadDetailView.as_view(), name='detail'),
    ], 'app_chat')

  