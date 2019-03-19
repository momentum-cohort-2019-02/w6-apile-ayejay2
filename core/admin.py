from django.contrib import admin
from core.models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'posted_on',
        'url',
    )
    exclude = ('slug',)
