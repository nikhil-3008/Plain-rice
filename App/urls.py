from django.urls import path
from .views import *

urlpatterns = [
    path('',Home,name="Home"),
    path('Profile',Profile,name='Profile'),
    path('investnow',investnow,name='investnow'),
    path('addfunds',addfunds,name='addfunds'),
    path('about',about,name='about'),
    path('dashboard1',dashboard1,name='dashboard1'),
]