from django.urls import path
from .views import *

urlpatterns = [
    path('',Home,name="Home"),
    path('Profile',Profile,name='Profile'),
    path('investnow',investnow,name='investnow'),
    path('investorinfo',investorinfo,name ='investorinfo'),
    path('dashboard1',dashboard1,name='dashboard1'),
    path('dashboard2',dashboard2,name='dashboard2'),
]