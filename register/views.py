from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# from .forms import *

# @TODO: Create register View

def register(request):
    form = UserCreationForm()
    return render(request, 'register/register.html', {'form': form})
