from django.urls import path
from todoapp.views import index, add_item, delete, turn_on, turn_off, account, authentification, delete_account

urlpatterns = [
    path('', account, name='account'),
    path('add/', add_item, name='add'),
    path('delete/<item>/', delete, name='delete'),
    # path('main/', index, name='main'),
    path('turn_On/<item>/', turn_on, name='turn_On'),
    path('turn_Off/<item>/', turn_off, name='turn_Off'),
    path('index/', index, name='index'),
    path('authentification/', authentification, name='authentification'),
    path('delete_account/', delete_account, name='delete_account'),
]
