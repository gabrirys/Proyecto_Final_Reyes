from django.urls import path, re_path
from .views import (mensajes_privados, DetailMs,CanalDetailView,Inbox)

UUID_CANAL_REGEX = r'canal/(?P<pk>[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12})'

urlpatterns = [
    re_path(UUID_CANAL_REGEX, CanalDetailView.as_view()),
    # path('chat/<str:username>', mensajes_privados, name='mensajes_privados'),
    path('chat/<str:username>', DetailMs.as_view(), name='detailms'),
    path("", Inbox.as_view(), name="inbox"),
]