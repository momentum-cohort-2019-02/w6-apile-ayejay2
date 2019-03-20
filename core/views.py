from django.shortcuts import render
from core.models import Post, Comment, Vote
from django.views.generic import View

# Create your views here.
def index(request):
    context = {

    }

    return render(request, 'index.html', context=context)
