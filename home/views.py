from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from register.views import login
from .models import *

from .forms import Place_OrderForm


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

def place_order(request):
    form = Place_OrderForm()

    if request.method == 'POST':
        form = Place_OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'update successful!')
            return redirect('order_details')

    context = {'form':form}
    return render(request, 'home/place_order.html', context)


