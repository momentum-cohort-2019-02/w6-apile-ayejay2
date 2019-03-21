from django.shortcuts import render, get_object_or_404, redirect
from core.models import Post, Comment, Vote
from django.views.generic import View
from django.views import generic
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_http_methods

from .forms import CommentForm

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

### TODO: in production --------------------->   

def create_comment(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.posted_by = request.user
            comment.created_at = timezone.now()
            comment.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'post_detail.html', {'form': form})

### TODO: In Production ------------------------------>
