from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django import forms

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .forms import CreateUserForm

# Create your views here.


class LogoutInterfaceView(LogoutView):
    success_url = "home/login"
    # template_name = "home/login.html"
    redirect_url = "/home/login"


# @method_decorator(login_required(login_url="/home/login"), name="get")
class LoginInterfaceView(LoginView):
    template_name = "home/login.html"
    fields = ('username', 'password')
    redirect_authenticated_user = "/home"


class SignupView(CreateView):
    form_class = CreateUserForm
    template_name = 'home/signup.html'
    success_url = 'home/login'

    def get(self, request, *args, **kwargs):
        # redirect the user to the home page has/is logged in
        if request.user.is_authenticated:
            return redirect('/home')
        return super().get(self, request, *args, **kwargs)


@method_decorator(login_required(login_url='/home/login'), name="get")
class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    # for extra content for the template literal
    extra_context = {'today': datetime.today()}
