from django.shortcuts import render
from django.http import HttpResponse

def epocket_home(request):
    return HttpResponse('Welcome to Epocket Home Page')

def home(request):
    template_name = 'home.html'
    return render(request, template_name)