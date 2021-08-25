from . import views
from django.urls import path

urlpatterns = [

    path('welcome',views.home,name='welcome'),
    path('register',views.reg,name='register'),
    path('login',views.log,name='login'),

]