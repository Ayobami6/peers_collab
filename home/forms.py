from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'placeholder': 'First Name', 'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'placeholder': 'Last Name', 'class': 'form-control'}))
    email = forms.EmailField(max_length=250, widget=forms.TextInput(
        attrs={'placeholder': 'Email', 'class': 'form-control',
               'pattern': '^[\\w\\d]([A-Za-z0-9._%+-]+)@\\w+\\.\\w+'}))
    password1 = forms.CharField(max_length=250, widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'class': 'form-control',
               'pattern': '^([^\\s][\\w]{7,})$'}))
    password2 = forms.CharField(max_length=250, widget=forms.PasswordInput(
        attrs={'placeholder': 'Retype Password', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Email'}),
            'username': forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Firstname'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Lastname'}),
        }

        labels = {
            "password2": "Confirm Password"
        }
