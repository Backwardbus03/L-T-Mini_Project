from django.db import models
from django.contrib.auth.models import User

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dateofbirth = models.DateField()

    def __str__(self):
        return self.user.username

def user_directory_path(instance, filename):
    # Files will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f'user_{instance.user.id}/{filename}'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)
    profile_picture = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    resume = models.FileField(upload_to=user_directory_path, blank=True, null=True)
    skills = models.TextField(blank=True)  # Comma-separated list like "ReactJS,Python"
    created_at = models.DateTimeField(auto_now_add=True)
    
    # return render(request, 'accounts/profile_edit.html', context)

    def __str__(self):
        return f"{self.user.username}'s profile"

    class Meta:
        get_latest_by = 'created_at'