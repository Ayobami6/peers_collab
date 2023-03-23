from django.contrib.auth.models import User
from django import forms
from ckeditor.fields import RichTextField
from . models import Posts


class PostForm(forms.ModelForm):

    class Meta:
        model = Posts
        fields = ('content', 'title')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
        }
        labels = {
            'content': 'Create a post'
        }
