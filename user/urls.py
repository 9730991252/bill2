from django.urls import  path
from .import views
urlpatterns = [
    path('user_home/', views.user_home, name='user_home'),
    path('bill/', views.bill, name='bill'),
    path('bill_in/<int:id>', views.bill_in, name='bill_in'),
    path('out/', views.out, name='out'),
    path('transfer/', views.transfer, name='transfer'),
    path('phonepe_verify/', views.phonepe_verify, name='phonepe_verify'),
    path('bill_in_verify/', views.bill_in_verify, name='bill_in_verify'),
    path('transfer_in_verify/', views.transfer_in_verify, name='transfer_in_verify'),
    path('bank_verify/', views.bank_verify, name='bank_verify'),
    path('bill_in_verify_bank/', views.bill_in_verify_bank, name='bill_in_verify_bank'),
    path('transfer_cash_to_bank/', views.transfer_cash_to_bank, name='transfer_cash_to_bank'),
    path('transfer_bank/', views.transfer_bank, name='transfer_bank'),
    path('bill_verify_admin/', views.bill_verify_admin, name='bill_verify_admin'),
]