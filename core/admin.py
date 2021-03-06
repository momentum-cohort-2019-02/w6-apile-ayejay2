from django.contrib import admin
from core.models import Post, Comment
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'posted_on',
        'url',
        'image_url',
    )
    exclude = ('slug',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Class that creates the way Comment info is displayed in Admin. Calls on Comment Model"""
    list_display = (
        'post', 
        'created_at',
        'text',
        )
