from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('search/', views.search, name='search'),
    path('post/<slug:slug>', views.blogpost, name='blog-post'),
   
    
  
 ]