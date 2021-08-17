from . import views
from django.urls import path

urlpatterns = [

    path('',views.home,name='home'),
    path('done/<int:id>/',views.delete,name='delete'),
    path('update/<int:taskid>/',views.update,name='update'),
    path('cbvhome/',views.TaskList.as_view(),name='cbvhome'),
    path('cbvupdate/<int:pk>/',views.TaskUpdate.as_view(),name='cbvupdate'),
    path('cbvdetail/<int:pk>/',views.TaskDetail.as_view(),name='cbvdetail'),
    path('cbvdelete/<int:pk>/', views.TaskDelete.as_view(), name='cbvdelete'),

]