from django.shortcuts import render, get_object_or_404, redirect
from core.models import Post, Comment, Vote
from django.views.generic import View
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your views here.
from core.forms import CommentForm, PostForm
from core.models import Post, Comment, Vote
from django.db.models import Max


def index(request):

    posts = Post.objects.all()
    comments = Comment.objects.all()
    votes = Vote.objects.all()
    vote_count = Post.objects.all().annotate(last_vote_date=Max('votes__voted_at')).order_by('-last_vote_date')
    context = {
        'posts': posts,
        'comments': comments,
        'votes': votes,
        'vote_count': vote_count,
    }
    return render(request, 'index.html', context=context)

class PostDetailView(generic.DetailView):
    model = Post


@require_http_methods(['GET', 'POST'])
@login_required
def create_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.posted_by = request.user
            comment.save()
            return redirect(post.get_absolute_url())
    else:
        form = CommentForm()
    template = 'core/add_comment.html'
    context = {'form': form}
    return render(request, template, context)


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

@require_http_methods(['GET', 'POST'])
@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect(post.get_absolute_url())
    else:
        form = PostForm()
    return render(request, 'core/post_new.html', {'form': form})

@login_required
def post_remove(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect('index')
