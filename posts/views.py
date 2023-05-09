from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import Posts
from . forms import PostForm
from django.http import HttpResponseRedirect
from django.urls import reverse


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
    # add ordering for created at
    ordering = ['-created_at']


class PostDetailView(DetailView):
    model = Posts
    context_object_name = "post"
    template_name = 'posts/posts_detail.html'

    def get_context_data(self, *args, **kwargs):
        # html template context
        context = super().get_context_data(**kwargs)
        post = get_object_or_404(Posts, id=self.kwargs['pk'])
        total_likes = post.total_likes()
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context


class PostsDeleteView(DeleteView):
    model = Posts
    success_url = 'home/posts'
    template_name = 'posts/posts_delete.html'


class PostUpdateView(UpdateView):
    model = Posts
    success_url = 'home/posts'
    form_class = PostForm
    template_name = "posts/create_post.html"


def LikeView(request, pk):
    post = get_object_or_404(Posts, id=request.POST.get('like'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))
