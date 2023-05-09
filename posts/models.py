from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.http import HttpRequest

# Create your models here.


# def get_user_username(request=HttpRequest):
#     user = request.META.get('REMOTE_USER')
#     return f"{user.username}"


class Posts(models.Model):

    title = models.CharField(max_length=200)
    content = RichTextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts_authors")
    likes = models.ManyToManyField(User, related_name='posts_likes')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f"Post {self.id} by {self.author.username}"
