from django.urls import path
from django.contrib import admin
from . import views



urlpatterns = [ 
        path('', views.index, name = 'index'),
        path('predictions/', views.predictions, name = 'predictions'),
        path('<slug:slug>/', views.post_detail, name = 'post'),
        
]

