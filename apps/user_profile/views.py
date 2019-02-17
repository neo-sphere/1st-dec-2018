from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

def user_profile_home(request):
    return HttpResponse('<h1>Welcome to User Profile Home Page</h1>')

def profile(request):
    template_name = 'profile.html'
    return render(request, template_name)

def signup(request):
    template_name = 'signup.html'
    if request.method == 'POST':
        form = UserCreationForm(request.POST) # form with data
        if form.is_valid():
            form.save()
            return redirect('home') # name of url 
    else:
        form = UserCreationForm() # empty form on get request 

    context = {
        'form': form,
    } 
    return render(request, template_name, context)
