from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('place_order/', views.place_order, name='order'),
    path('order_details/', views.order_details, name='order_details'),
    path('profile', views.profile, name='profile'),
    # path('place_order', views.delivery_page, name="place_order"),
]
