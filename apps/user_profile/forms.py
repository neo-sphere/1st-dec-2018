from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    mobile_no = forms.CharField(max_length=15)
    balance = forms.IntegerField()

    class Meta:
        model = User
        fields = ('username', 'email', 'mobile_no', 'balance')