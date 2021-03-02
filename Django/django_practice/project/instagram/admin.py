from django.contrib import admin
from .models import Post
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
    list_display = ['message', 'message_length']
    search_fields = ['message']
    list_filter = ['message']


    def message_length(self, post):
        return len(post.message)

    message_length.short_description = "메시지 글자수"



