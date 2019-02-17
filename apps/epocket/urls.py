from django.urls import path

from .views import epocket_home

urlpatterns = [
    path('home/', epocket_home),
]