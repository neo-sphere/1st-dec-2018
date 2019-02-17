from django.shortcuts import render
from django.http import HttpResponse

def epocket_home(request):
    return HttpResponse('Welcome to Epocket Home Page')