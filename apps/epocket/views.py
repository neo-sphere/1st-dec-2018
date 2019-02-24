from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView

from apps.user_profile.models import Profile

from .models import Transaction
from .forms import BalanceTransferForm

def epocket_home(request):
    return HttpResponse('Welcome to Epocket Home Page')

def home(request):
    template_name = 'home.html'
    return render(request, template_name)


class BalanceTransfer(CreateView):
    template_name = 'balance_transfer.html'
    form_class = BalanceTransferForm
    success_url = '/'

    def form_valid(self, form):
        mobile = form.cleaned_data.get('mobile') # cleaned_data is a dictionary 
        temp = form.save(commit=False) #  temp instance of form object, doesn't save instace in db
        temp.from_user = self.request.user
        temp.to_user = Profile.objects.get(contact_no=mobile).user
        temp.save()
        return super().form_valid(form)
