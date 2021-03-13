from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Profile
# from django.contrib.auth import get_user_model


admin.site.register(User, UserAdmin)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'user', 'user_photo', 'status_message']