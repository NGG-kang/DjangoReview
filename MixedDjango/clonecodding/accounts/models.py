from django.contrib.auth.models import AbstractUser
from django.db import models
from django_boost.models.fields import AutoOneToOneField
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    # following_set = models.ManyToManyField("self", blank=True)
    # follower_set = models.ManyToManyField("self", blank=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254, blank=True)


# def user_profile_path(instance, filename):
#     return 'instagram/user_{}/{}'.format(instance.name, filename)
#
#
# class Profile(models.Model):
#     userid = AutoOneToOneField(get_user_model(), related_name='profile', on_delete=models.CASCADE)
#     user_photo = models.ImageField(blank=True, upload_to=user_profile_path)
#     status_message = models.CharField(blank=True, max_length=300)
