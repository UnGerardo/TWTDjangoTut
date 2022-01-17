from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    #need this class to say when using RegisterForm and saving it, save it to the users database
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]