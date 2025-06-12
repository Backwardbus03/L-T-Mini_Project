from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate
from .models import CustomUser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
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

