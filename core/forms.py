from django import forms
from core.models import Post, Comment

class CommentForm(forms.Form):
### TODO: Basic Form for Comment. need to build out. ###
    comment = forms.CharField(widget=forms.Textarea(attribute="..."))
