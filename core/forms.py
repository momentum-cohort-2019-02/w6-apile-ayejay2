from django import forms
from core.models import Post, Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.TextInput(attrs={'style': 'width: 400px'}),
        }


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'url', 'description', 'image_url')
