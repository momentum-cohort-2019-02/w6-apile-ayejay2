from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<slug:slug>', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<slug:slug>/vote/', views.post_vote_view, name="vote_posts"),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<slug:slug>/remove/', views.post_remove, name="post_remove")
    path('post/<slug:slug>/comment/', views.create_comment, name='create_comment'),

]
