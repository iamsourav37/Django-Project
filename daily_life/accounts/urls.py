from django.urls import path
from . import views


urlpatterns = [
    
    path('signup/', views.signup,name='signup-page'),
    path('login/', views.login,name='login-page'),
    path('logout/', views.logout,name='logout'),

]
