from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('order/', views.order, name='order'),
    path('order_details/', views.order_details, name='order_details'),
    path('profile', views.profile, name='profile'),
]
