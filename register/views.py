from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# from .forms import *

# @TODO: Create register View

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}, Please logIn!')
            return redirect('index')
    else :
        form = UserCreationForm()
    return render(request, 'register/register.html', {'form': form})
