from django.urls import path

from .views import epocket_home, BalanceTransfer, UserBasedTransactionListView

urlpatterns = [
    path('home/', epocket_home),
    path('transfer/', BalanceTransfer.as_view(), name='balance-transfer'),
    path('transaction/detail/', UserBasedTransactionListView.as_view(), name='transaction-list'),
]