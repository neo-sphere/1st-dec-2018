from django.urls import path

from .views import epocket_home, BalanceTransfer

urlpatterns = [
    path('home/', epocket_home),
    path('transfer/', BalanceTransfer.as_view(), name='balance-transfer'),
]