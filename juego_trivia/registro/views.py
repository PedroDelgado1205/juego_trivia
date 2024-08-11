from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UserForm

def home(request):
    return render(request, 'registro/home.html')

def register_view(request):
    return render(request, 'registro/register.html')

def login_view(request):
    if request.method == 'POST':
        form = UserForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('juego:game')  
    else:
        form = UserForm()
    return render(request, 'registro/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  
