from django.db import models
import datetime
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.files import File
import os
import PIL


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    url = models.URLField(max_length=255)
    posted_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    description = models.CharField(max_length=255, null=True)
    image_file = models.ImageField(upload_to='images', null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    #there are many users who will have many votes
    #go to User 
    voted_by = models.ManyToManyField(to=User, related_name='vote_posts', through='Vote')
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', default=1)


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

    
    def get_remote_image(self):
        if self.image_url and not self.image_file:
            result = urllib.urlretreive(self.image_url)
            self.image_file.save(
                os.path.basename(self.image_url),
                File(open(result[0], 'rb'))
            )
        self.save()


class Comment(models.Model):
    """Model representing Comments on a Post"""

    post = models.ForeignKey(to=Post, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField('')
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', default=1)


    def __str__(self):
        return self.text


class Vote(models.Model):
    """Model representing a vote."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    voted_at = models.DateTimeField(auto_now_add=True)
