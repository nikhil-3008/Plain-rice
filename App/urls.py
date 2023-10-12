from django.urls import path
from .views import *

urlpatterns = [
    path('',Home,name="Home"),
    path('portfolio',Portfolio,name='portfolio'),
    path('investnow',investnow,name='investnow'),
    path('addfunds',addfunds,name='addfunds'),
    path('about',about,name='about'),
]