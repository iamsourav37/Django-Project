from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='todo-home'),
    path('view/',views.view_list,name='todo-view'),
    path('add/',views.add_new,name='todo-add'),
    path('delete/<int:id>',views.delete,name='todo-delete'),
]