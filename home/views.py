from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView

# Create your views here.


class LoginInterfaceView(LoginView):
    template_name = "home/login.html"


class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    # for extra content for the template literal
    extra_context = {'today': datetime.today()}
