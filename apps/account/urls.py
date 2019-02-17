from django.urls import path

from .views import account_home

urlpatterns = [
    path('home/', account_home),
]