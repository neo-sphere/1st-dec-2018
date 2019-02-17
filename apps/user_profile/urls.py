from django.urls import path

from .views import user_profile_home

urlpatterns = [
    path('home/', user_profile_home),
]