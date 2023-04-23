from logging import PlaceHolder
from django import forms
from django.forms import ModelForm
from forum.models import Post

class PostForm(ModelForm):
    title = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Post Title'}), required = True)
    content = forms.CharField(widget = forms.Textarea(attrs={'placeholder': 'Type your question here...'}), required = True)
    class Meta:
        model = Post
        fields = ['title', 'content']    