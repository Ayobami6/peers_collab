from django.urls import path

from . import views

urlpatterns = [
    path('home/ask', views.ask_gpt, name='ask'),
]
