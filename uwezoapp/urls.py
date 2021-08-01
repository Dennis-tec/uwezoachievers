from django.contrib.admin.decorators import register
from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = 'index'),
    path('login', views.login, name = 'login'),
    path('register', views.register, name ='register'),
    path('logout', views.logout, name = 'logout'),
    path('whatwedo', views.whatwedo, name = 'whatwedo'),
    path('goal', views.goal, name = 'goal'),
    path('high', views.high, name = 'high'),
    path('kenyan', views.kenyan, name = 'kenyan'),
    path('abroad', views.abroad, name = 'abroad'),
    path('news', views.news, name = 'abroad')

]