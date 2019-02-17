from django.shortcuts import render
from django.http import HttpResponse

def user_profile_home(request):
    return HttpResponse('Welcome to User Profile Home Page')
