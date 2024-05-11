from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import path,include

urlpatterns = [
    path('', views.index, name='index'),
     path('support/', views.support, name='support'),
 
    
   
       
]
