from django.urls import path

from .views import user_profile_home, profile, signup

urlpatterns = [
    path('home/', user_profile_home),
    path('profile/', profile),
    path('signup/', signup),
]