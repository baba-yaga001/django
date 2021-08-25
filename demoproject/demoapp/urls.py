from . import views
from django.urls import path

urlpatterns = [

    path('',views.home,name='home'),
    path('welcome',views.welcome,name='welcome'),
    path('register',views.reg,name='register'),
    path('login',views.log,name='login'),
    path('logout',views.logout,name='logout')

]