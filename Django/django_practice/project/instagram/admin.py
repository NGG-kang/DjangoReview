from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post, Comment, Tag
# Register your models here.

# 1번
# admin.site.register(Post)

# 2번
# class PostAdmin(admin.ModelAdmin):
#     pass
#
# admin.site.register(Post,PostAdmin)

# 3번

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['message', 'message_length','photo_tag']
    search_fields = ['message']
    list_filter = ['message']

    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f"<img src='{post.photo.url}' />")
        return None

    def message_length(self, post):
        return len(post.message)

    message_length.short_description = "메시지 글자수"



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass