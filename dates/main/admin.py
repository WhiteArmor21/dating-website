from django.contrib import admin
from .models import *
from main.models import UserProfile


admin.site.register(UserMatch)
#admin.site.register(UserProfile)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = [
        'username',
        'gender',
    ]