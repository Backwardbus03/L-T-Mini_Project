from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import datetime

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text='Required. Please enter a valid email address.')
    dateofbirth = forms.DateField(initial=datetime.date.today, help_text='Required. Please enter a valid date of birth.')

    class Meta:
        model = User
        fields = ('username', 'email', 'dateofbirth', 'password1', 'password2')