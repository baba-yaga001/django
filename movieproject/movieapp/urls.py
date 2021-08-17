from django.urls import path
from . import views
app_name = 'movieapp'

urlpatterns = [
    path('',views.index,name='index'),
    path('movie/<int:id>',views.details,name='details'),
    path('add/',views.add_movie,name='add'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('delete/<int:id>/', views.delete, name='delete')

]