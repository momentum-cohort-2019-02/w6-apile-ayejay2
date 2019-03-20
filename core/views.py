from django.shortcuts import render
from core.models import Post, Comment, Vote
from django.views.generic import View

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context=context)
