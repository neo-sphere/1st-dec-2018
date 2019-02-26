
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

from django.conf import settings

from apps.account.models import Account
from .models import Profile
from .forms import CustomUserCreationForm

def user_profile_home(request):
    return HttpResponse('<h1>Welcome to User Profile Home Page</h1>')

def profile(request):
    template_name = 'profile.html'
    return render(request, template_name)

def signup(request):
    template_name = 'signup.html'
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST) # form with data
        if form.is_valid():
            mobile = form.cleaned_data.get('mobile_no')
            u = form.save()
            Profile.objects.create(user=u, contact_no=mobile)
            Account.objects.create(user=u)
            return redirect('home') # name of url 
    else:
        form = CustomUserCreationForm() # empty form on get request 
        print('form get method')

    context = {
        'form': form,
    } 
    return render(request, template_name, context)


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = settings.LOGIN_REDIRECT_URL

    def form_valid(self, form):
        mobile = form.cleaned_data.get('mobile_no')
        balance = form.cleaned_data.get('balance')
        user = form.save()
        Profile.objects.create(user=user, contact_no=mobile)
        Account.objects.create(user=user, balance=balance)
        
        return super().form_valid(form)
