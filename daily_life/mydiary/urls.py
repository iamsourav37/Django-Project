from django.urls import path
from . import views

urlpatterns = [
    path('',views.diary_index,name='diary-home' ),
    path('view/',views.view_all_content,name='diary-view' ),
    path('add/',views.add_new_content,name='diary-add' ),
    path('delete/<int:id>',views.delete_content,name='diary-delete' ),

]