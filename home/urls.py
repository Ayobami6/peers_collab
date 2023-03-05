from django.urls import path

from . import views

urlpatterns = [
    path('home/login', views.LoginInterfaceView.as_view(), name='login'),
    path('home', views.HomeView.as_view(), name='home'),
    path('register', views.SignupView.as_view(), name='signup'),
    path('logout', views.LogoutInterfaceView.as_view(), name='logout'),
]
