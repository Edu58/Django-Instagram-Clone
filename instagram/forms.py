from dataclasses import fields
from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'
        
        
class LoginUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1']