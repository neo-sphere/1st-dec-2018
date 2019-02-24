from django import forms

from .models import Transaction

class BalanceTransferForm(forms.ModelForm):
    mobile = forms.CharField(max_length=15)

    class Meta:
        model = Transaction
        fields = ('mobile', 'balance')

