from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from app_perfiles.forms import UserRegisterForm
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import UpdateView
from app_perfiles.forms import UserRegisterForm, UserUpdateForm, AvatarFormulario

class CustomLogoutView(LogoutView):
   template_name = 'perfiles/logout.html'


#REGISTRO
def registro(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            formulario.save()  # Esto lo puedo usar porque es un model form
            url_exitosa = reverse('inicio')
            return redirect(url_exitosa)
    else:  # GET
        formulario = UserRegisterForm()
    return render(
        request=request,
        template_name="perfiles/registro.html",
        context={'form': formulario},
   )

