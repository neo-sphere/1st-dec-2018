from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView

from .models import Transaction

def epocket_home(request):
    return HttpResponse('Welcome to Epocket Home Page')

def home(request):
    template_name = 'home.html'
    return render(request, template_name)


class BalanceTransfer(CreateView):
    template_name = 'balance_transfer.html'
    model = Transaction
    fields = '__all__'
    success_url = '/'
