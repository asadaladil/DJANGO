from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='Home Page'),
    path('signup/', views.signup,name='signup'),
    path('login/', views.Login,name='login'),
    path('profile/', views.profile,name='profile'),
    path('logout/', views.Logout,name='logout'),
    path('passchange/', views.pass_change,name='passchange'),
    path('passchange2/', views.pass_change2,name='passchange2'),
    path('changedate/', views.change_user_data,name='changedata'),
]