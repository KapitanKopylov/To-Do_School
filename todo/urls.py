from django.urls import path
from todoapp.views import index, add_item, delete, turn_On, turn_Off, add_user, account, authentification, main

urlpatterns = [
    path('', account, name='account'),
    path('add/', add_item, name='add'),
    path('delete/<item>/', delete, name='delete'),
    path('main/', index, name='main'),
    path('turn_On/<item>/', turn_On, name='turn_On'),
    path('turn_Off/<item>/', turn_Off, name='turn_Off'),
    path('index/', index, name='index'),
    path('authentification/', authentification, name = 'authentification'),
]