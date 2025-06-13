from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'first_name', 'last_name', 'phone', 'email', 'location', 'bio',
            'profile_picture', 'resume', 'skills'
        ]
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Tell us about yourself'}),
            'skills': forms.TextInput(attrs={'placeholder': 'e.g. Python, ReactJS'}),
        }
