from django.urls import  path
from .import views
urlpatterns = [
    path('office_home/', views.office_home, name='office_home'),
    path('user/', views.user, name='user'),
    path('type/', views.type, name='type'),
    path('phonepe/', views.phonepe, name='phonepe'),
    path('bank_account/', views.bank_account, name='bank_account'),
]