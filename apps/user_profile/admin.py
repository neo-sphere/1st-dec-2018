from datetime import date

from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('contact_no', 'address', 'nationality', 'gender', 'dob', 'occupation', 'get_age')

    def get_age(self, instance):
        timedelta_obj = date.today() - instance.dob
        return int(timedelta_obj.days // 365.25)

    get_age.short_description = 'Age'

# admin.site.register(Profile, ProfileAdmin) # old style


