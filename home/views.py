from django.shortcuts import render
from .models import *

def index(request):
    return render(request, 'index.html', {})

# get Order details 
def order_details(request):
    orders = Place_Order.objects.all()
    return render(request,'order/order_details.html', {'orders':orders})

def order(request):
    return render(request, 'order/order.html')

def profile(request):
    user_info = User.objects.all()
    return render(request, 'order/profile.html', {'user_info':user_info})