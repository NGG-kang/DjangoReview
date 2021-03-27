from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Post, Comment, Tag
# Register your models here.


admin.site.register(Tag)


@admin.register(Post)
class PostAdmin(ModelAdmin):
    list_display = ['author', 'message']


@admin.register(Comment)
class CommentAdmin(ModelAdmin):
    list_display = ['author', 'post', 'comment']