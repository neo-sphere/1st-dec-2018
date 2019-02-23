from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import user_profile_home, profile, signup, SignUpView

urlpatterns = [
    path('', user_profile_home, name='home'),
    path('profile/', profile, name='profile'),
    path('signup/', signup, name='signup'),
    path('csignup/', SignUpView.as_view(), name='csignup'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
