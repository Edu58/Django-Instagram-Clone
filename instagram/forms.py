from dataclasses import fields
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password2 = forms.EmailField(required=False)
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name','username', 'password1']
        
        
class LoginUserForm(UserCreationForm):
    username = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ['username', 'password1']