from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from .models import CustomUser


def home(request):
    return HttpResponse("<h1>Welcome to the home page!</h1>")


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            dateofbirth = form.cleaned_data.get('dateofbirth')
            CustomUser.objects.create(user=user, dateofbirth=dateofbirth)
            return render(request, 'accounts/signup.html')

    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to a home page or dashboard
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})
