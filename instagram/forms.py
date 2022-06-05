from dataclasses import fields
from operator import mod
from pyexpat import model
from django import forms
from django.forms import DateField, ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Image


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
        
    
    
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_photo', 'bio', 'location', 'birth_date']
        
        

class UploadForm(ModelForm):
    class Meta:
        model = Image
        fields = ['image_name', 'image', 'image_caption']