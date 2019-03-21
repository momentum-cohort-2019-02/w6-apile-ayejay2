from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<slug:slug>', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<slug:slug>/vote/', views.post_vote_view, name="vote_posts")
]
