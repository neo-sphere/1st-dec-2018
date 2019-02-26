from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.core.exceptions import ValidationError
from .models import Profile


class CustomUserCreationForm(UserCreationForm):
    mobile_no = forms.CharField(max_length=15)
    balance = forms.IntegerField()

    class Meta:
        model = User
        fields = ('username', 'email', 'mobile_no', 'balance')

    def clean_balance(self):
        balance = self.cleaned_data.get('balance')
        if balance < 0 or balance > 1000:
            raise ValidationError(('invalid amount!'))
        else:
            return balance

    # To validate emil User.objects.filter(email=mail).exists()
    # pre validate
    def clean_mobile_no(self):
        mobile = self.cleaned_data.get('mobile_no')
        is_number_used = Profile.objects.filter(contact_no=mobile).exists()
        print(is_number_used)
        if is_number_used:
            raise ValidationError(
                    ('Phone no : %(value)s already used!'),
                        params={'value': mobile},
                    )
        else:
            return mobile
