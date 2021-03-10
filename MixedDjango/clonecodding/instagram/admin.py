from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Post, Comment, Tag
# Register your models here.

admin.site.register(Comment)
admin.site.register(Tag)

@admin.register(Post)
class PostAdmin(ModelAdmin):
    list_display = ['author', 'message']