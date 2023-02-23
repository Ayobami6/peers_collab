from django.urls import path

from . import views

urlpatterns = [
    path('', views.LoginInterfaceView.as_view(), name='login'),
    path('home', views.HomeView.as_view(), name='home'),
]
