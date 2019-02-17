from django.shortcuts import render
from django.http import HttpResponse

def user_profile_home(request):
    return HttpResponse('<h1>Welcome to User Profile Home Page</h1>')

def profile(request):
    template_name = 'profile.html'
    return render(request, template_name)