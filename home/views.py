from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from register.views import login
from .models import *

def index(request):
    return render(request, 'index.html', {})

# get Order details 
@login_required
def order_details(request):
    orders = Place_Order.objects.all()
    return render(request,'home/details.html', {'orders':orders})

@login_required
def place_order(request):
    return render(request, 'home/place_order.html')

@login_required
def profile(request):
    # user_info = User.objects.filter().first()
    return render(request, 'register/profile.html', {})


