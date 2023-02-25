from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django import forms


from . forms import CreateUserForm
# Create your views here.


class LoginInterfaceView(LoginView):
    template_name = "home/login.html"
    fields = ('username', 'password')


# def signup(request):
#     if request.method == "POST":
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home/')

#         else:
#             form = CreateUserForm()

#         return render(request, 'signup.html', {'form': form})


class SignupView(CreateView):
    form_class = CreateUserForm
    template_name = 'home/signup.html'
    success_url = 'home/login'


class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    # for extra content for the template literal
    extra_context = {'today': datetime.today()}
