from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import Posts
from . forms import PostForm


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Posts
    success_url = '/home'
    form_class = PostForm
    login_url = '/home/login'
    template_name = "posts/create_post.html"
