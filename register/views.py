from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import *

# @TODO: Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('order')
        else:
            messages.success(request, "Error logging In, try again")
            return redirect('login')
    else:
        return render(request, 'login.html', {})

# @TODO: Create logout route 
def logout_user(request):
    logout(request)
    messages.success(request, "Successfully logged out!")
    return redirect('index')


# @TODO: Create register route 
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request, user)
            messages.success(request,("User Successfully Created. Login!"))
            return redirect('login')
        else:
            form = UserCreationForm()
            return render(request,'register.html', form)
