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
    # fields = '__all__'
    login_url = '/home/login'
    template_name = "posts/create_post.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostListView(LoginRequiredMixin, ListView):
    model = Posts
    context_object_name = 'posts'  # default object
    # can pass template name if need be or not
    template_name = "posts/welcome.html"
    login_url = "/login"
