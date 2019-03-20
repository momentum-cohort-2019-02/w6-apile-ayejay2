from django.contrib import admin
from core.models import Post, Comment
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'posted_on',
        'url',
    )
    exclude = ('slug',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'post', 
        'created_at'
        )