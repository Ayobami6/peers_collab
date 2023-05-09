from django.urls import path

from . import views

urlpatterns = [
    path('home/create_post', views.CreatePostView.as_view(),
         name='create_post'),
    path('home/posts', views.PostListView.as_view(), name='post_list'),
    path('home/posts/<int:pk>', views.PostDetailView.as_view(),
         name='post_detail'),
    path('home/posts/<int:pk>/delete', views.PostsDeleteView.as_view(),
         name='post_delete'),
    path('home/posts/<int:pk>/edit',
         views.PostUpdateView.as_view(), name='post_update'),
    path('home/like/<int:pk>', views.LikeView, name="like_post"),
]
