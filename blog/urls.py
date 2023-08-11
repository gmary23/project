#from blog import views as blog_views # esse acrescentou
#from django.contrib import admin
#from django.http import HttpResponse
from blog import views 
from django.urls import path



urlpatterns = [
    path('', views.blog),
    path('exemplo/', views.exemplo),
 
]