from django.shortcuts import render
from django.http import HttpResponse

def account_home(request):
    return HttpResponse('Welcome to Account Home Page')
