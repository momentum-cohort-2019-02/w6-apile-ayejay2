from django.shortcuts import render, get_object_or_404, redirect
from core.models import Post, Comment, Vote
from django.views.generic import View
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from core.forms import CommentForm, PostForm
from django.contrib.auth.models import User
from .forms import CommentForm
from django.utils.text import slugify
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
### TODO: In Production ------------------------------> ^^^^^

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

@require_http_methods(['POST'])
@login_required
def post_new(request):
    if request.method == "POST":
        post = form.save(commit=False)
        post.voted_by = request.User
        post.slug = slugify('title')
        post.posted_on = timezone.now()
    else:
        form = PostForm(request.POST)
    return render(request, 'post_new.html', {'form': form})
