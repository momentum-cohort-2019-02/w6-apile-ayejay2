from django import forms
from core.models import Post, Comment

class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(attribute="..."))
