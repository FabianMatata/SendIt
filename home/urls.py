from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('home/', views.home),
    path('delivery', views.delivery),
    path('order/', views.order),
    # path('details/', views.details),
    path('details/', views.details, name="details"),
    path('changedestination/', views.changedestination, name="changedestination"),
]
