from django.urls import path
from django.contrib.auth.views import LoginView 

from .views import user_profile_home, profile, signup

urlpatterns = [
    path('home/', user_profile_home, name='user-profile-home'),
    path('profile/', profile, name='profile'),
    path('signup/', signup, name='signup'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
]