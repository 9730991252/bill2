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
    path('bill_in_verify_phonepe', views.bill_in_verify_phonepe, name='bill_in_verify_phonepe'),
    path('transfer_verify_phonepe', views.transfer_verify_phonepe, name='transfer_verify_phonepe'),
    path('bill_in_verify_bank', views.bill_in_verify_bank, name='bill_in_verify_bank'),
    path('transfer_verify_cash_to_bank', views.transfer_verify_cash_to_bank, name='transfer_verify_cash_to_bank'),
    path('transfer_verify_bank', views.transfer_verify_bank, name='transfer_verify_bank'),
    path('edit_bill_name', views.edit_bill_name, name='edit_bill_name'),
    path('admin_bill_verify', views.admin_bill_verify, name='admin_bill_verify'),
]