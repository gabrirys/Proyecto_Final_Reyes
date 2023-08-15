from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from .models import Chat, Message
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class ChatListView(ListView):
    model = Chat
    template_name = 'chat/chat_list.html'
    context_object_name = 'chats'

@method_decorator(login_required, name='dispatch')
class ChatDetailView(DetailView):
    model = Chat
    template_name = 'chat/chat_detail.html'
    context_object_name = 'chat'

@method_decorator(login_required, name='dispatch')
class MessageCreateView(CreateView):
    model = Message
    fields = ['texto']
    template_name = 'chat/message_create.html'

    def form_valid(self, form):
        chat_id = self.kwargs['chat_id']
        chat = Chat.objects.get(id=chat_id)
        form.instance.chat = chat
        return super().form_valid(form)

    def get_success_url(self):
        chat_id = self.kwargs['chat_id']
        return reverse('chat_detail', args=[chat_id])
