from django.shortcuts import render, get_object_or_404, redirect
from core.models import Post, Comment, Vote
from django.views.generic import View
from django.views import generic
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):

    posts = Post.objects.all()
    comments = Comment.objects.all()
    votes = Vote.objects.all()
    context = {
        'posts': posts,
        'comments': comments,
        'votes': votes,
    }
    return render(request, 'index.html', context=context)

# class PostDetailView(generic.DetailView):
#     model = Post
    
    
    
# def post_detail_view(request, post_pk):
#     posts = get_object_or_404(Post, pk=post_pk)

#     context = {
#         'posts': posts,
#     }

#     return render(request, 'post_detail', context=context)
    

