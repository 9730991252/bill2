from django.urls import  path
from .import views
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('office_logout/', views.office_logout, name='office_logout'),
    path('user_logout/', views.user_logout, name='user_logout'),
]