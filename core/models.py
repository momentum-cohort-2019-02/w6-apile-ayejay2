from django.db import models
import datetime
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    url = models.URLField(max_length=255)
    posted_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ['-posted_on']
    
    def save(self, *args, **kwargs):
        self.set_slug()
        super().save(*args, **kwargs)
    
    def set_slug(self):
        if self.slug:
            return
        
        base_slug = slugify(self.title)
        slug = base_slug
        n = 0

        while Post.objects.filter(slug=slug).count():
            n += 1
            slug = base_slug + "-" + str(n)
        
        self.slug = slug
    
    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.slug)])

class Comment(models.Model):
    """Model representing Comments on a Post"""

    post = models.ForeignKey(to=Post, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(null=True, auto_now_add=True)
