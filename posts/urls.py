from django.urls import path

from . import views

urlpatterns = [
    path('home/create_post', views.CreatePostView.as_view(), name='create_post'),
    path('home/posts', views.PostListView.as_view(), name='post_list'),
]
