from django.contrib import admin

from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user', 'balance', 'created')