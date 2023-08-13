from django.http import HttpResponse
from django.shortcuts import render


def inicio(request):
    httpResponse = render(
        request=request,
        template_name="inicio.html",
        context={}
        )
    return httpResponse
    
def about(request):
    httpResponse = render(
        request=request,
        template_name="about.html",
        context={}
        )
    return httpResponse