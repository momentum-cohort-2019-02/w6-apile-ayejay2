from django.urls import path
from . import views
# from core import view as core_views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<slug:slug>', views.PostDetailView.as_view(), name='post-detail'),
    # path('post/<slug:slug_id>', views.create_comment, name='post-detail'),
]
