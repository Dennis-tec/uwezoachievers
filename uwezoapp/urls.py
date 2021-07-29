from django.contrib.admin.decorators import register
from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = 'index'),
    path('login', views.login, name = 'login'),
    path('register', views.register, name ='register'),
    path('logout', views.logout, name = 'logout')
]