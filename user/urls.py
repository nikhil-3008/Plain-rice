from django.contrib import admin
from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home,name='Home'),
    path('about/',about,name='about'),
    path('login/',Login,name='login'),
    path('logout/',Logout,name='logout'),
    path('OtpVerification/',OtpVerification,name='OtpVerification'),
    path('login/signup/',signup,name='signup'),
    path('signup/login/',Login,name='login'),
    path('signup/',signup,name='signup'),]+ static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])