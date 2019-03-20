from django.shortcuts import render
from core.models import Post, Comment, Vote
from django.views.generic import View

# Create your views here.
def index(request):
    posts = Post.objects.all()
    comments = Comment.objects.all()
    votes = Vote.objects.all()
    context = {
        'posts': posts,
        'comments': comment,
        'votes': votes,
    }
    return render(request, 'index.html', context=context)
