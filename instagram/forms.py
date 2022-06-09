from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Image, Comments


class SignUpForm(UserCreationForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password2 = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'username', 'password1']


class LoginUserForm(UserCreationForm):
    username = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'password1']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_photo', 'bio', 'location', 'birth_date']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'})
        }


class UploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image_name', 'image', 'image_caption', 'profile']
        exclude = ['profile', 'created_on']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment', 'image']
        exclude = ['profile', 'created_on', 'image']


class UserUpdateForm(forms.ModelForm):
    email= forms.EmailField()
    class Meta:
        model = User
        fields = ["username","email"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["profile_photo", "birth_date", "bio", "location"]