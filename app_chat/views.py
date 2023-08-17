from typing import Any, Optional
from django.db import models
from django.db.models.query import QuerySet
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Thread
from django.http import Http404

@method_decorator(login_required, name='dispatch')
class ThreadListView(ListView): # Utilizaremos una templateview
    model = Thread
    template_name = "app_chat/thread_list.html"

# Esta es otra manera de hacerlo
#class ThreadListView(ListView):
    
#    model = Thread
    
#    def get_queryset(self):
#        queryset = super(ThreadListView, self).get_queryset()
#        return queryset.filter(user=self.request.user)
    
@method_decorator(login_required, name='dispatch')   
class ThreadDetailView(DetailView):
    model = Thread
    
    def get_object(self):
        obj = super(ThreadDetailView, self).get_object()
        if self.request.user not in obj.user.all():
            raise Http404()
        return obj
    
    



