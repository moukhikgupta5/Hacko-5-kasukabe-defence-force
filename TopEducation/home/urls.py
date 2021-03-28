from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.loginuser,name='login'),
    path('logout',views.logoutuser,name='logout'),
    path('index',views.index,name = 'profile'),
    path('courseA',views.course,name = 'courseA'),
    path('courseB',views.course,name = 'courseB'),
    path('coursec',views.course,name = 'courseC'),
]
