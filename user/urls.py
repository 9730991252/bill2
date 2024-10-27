from django.urls import  path
from .import views
urlpatterns = [
    path('user_home/', views.user_home, name='user_home'),
    path('bill/', views.bill, name='bill'),
    path('bill_in/<int:id>', views.bill_in, name='bill_in'),
    path('out/', views.out, name='out'),
    path('transfer/', views.transfer, name='transfer'),
]