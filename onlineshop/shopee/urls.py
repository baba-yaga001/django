from django.urls import path,include
from . import views

app_name = 'shopee'

urlpatterns = [

    path('',views.allProCat,name="allProCat"),
    path('<slug:c_slug>/',views.allProCat,name = "product_byCAt"),
    path('<slug:c_slug>/<slug:pro_slug>/', views.proCat,name="proCat")

]