from django.contrib import admin
from accounts.models import *

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(UserProfile)