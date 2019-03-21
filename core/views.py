from django.shortcuts import render, get_object_or_404, redirect
from core.models import Post, Comment, Vote
from django.views.generic import View
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

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

class PostDetailView(generic.DetailView):
    model = Post
    
    
    
# def post_detail_view(request, post_pk):
#     posts = get_object_or_404(Post, pk=post_pk)

#     context = {
#         'posts': posts,
#     }

#     return render(request, 'post-detail', context=context)
    










@require_http_methods(['POST'])
@login_required
def post_vote_view(request, slug):
    post = get_object_or_404(Post, slug=slug)

    vote, created = request.user.vote_set.get_or_create(post=post)
    next = request.POST.get('next', '/')
    if created:
        messages.success(request, f"You have voted for {post.title}.")
    else:
        messages.info(request, f"You have redacted your vote for {post.title}.")
        vote.delete()
    return HttpResponseRedirect(next)
