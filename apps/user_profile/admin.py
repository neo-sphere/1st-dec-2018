from datetime import date

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile
from apps.account.models import Account

admin.site.unregister(User)

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class AccountInline(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = 'Account'
    fk_name = 'user'

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, AccountInline)
    list_display = ('username', 'get_contact', 'email', 'first_name', 'last_name', 'is_staff', 'get_balance')
    list_select_related = ('profile', 'account')

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)
    
    def get_contact(self, instance):
        return instance.profile.contact_no

    get_contact.short_description = 'Mobile'

    def get_balance(self, instance):
        return instance.account.balance

    get_balance.short_description = 'Available Balance'


