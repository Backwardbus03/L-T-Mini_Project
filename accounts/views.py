from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from .models import CustomUser


# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        email = request.POST.get('email')
        dateofbirth = request.POST.get('dob')

        if not User.objects.filter(username=username).exists():
            user = User.objects.create(username=username, password=password, email=email)
            CustomUser.objects.create(user=user, dateofbirth=dateofbirth)
        else:
            messages.error(request, 'Username already exists, please go to login page')

        return render(request, 'accounts/signup.html')

    return render(request, 'accounts/signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Username does not exist')
            return redirect('/accounts/login')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'accounts/login.html')
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')