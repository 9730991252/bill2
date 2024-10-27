from django.urls import  path
from .import views
urlpatterns = [
    path('out_user_cash', views.out_user_cash, name='out_user_cash'),
    path('out_user_phonepe', views.out_user_phonepe, name='out_user_phonepe'),
    path('out_bank', views.out_bank, name='out_bank'),
    path('transfer_user_cash', views.transfer_user_cash, name='transfer_user_cash'),
    path('transfer_user_phonepe', views.transfer_user_phonepe, name='transfer_user_phonepe'),
    path('transfer_user_bank', views.transfer_user_bank, name='transfer_user_bank'),
    path('transfer_user_cash_to_bank', views.transfer_user_cash_to_bank, name='transfer_user_cash_to_bank'),
    path('search_bill', views.search_bill, name='search_bill'),
]