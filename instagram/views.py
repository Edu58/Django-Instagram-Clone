from re import U
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm, LoginUserForm, ProfileForm, UploadForm
from django.contrib import messages
from .models import Image, Profile, Comments, Likes 

# Create your views here.
def home(request):
    all_posts = Image.objects.all()
    return render(request, 'index.html', {'posts': all_posts})


def profile(request):
    form = ProfileForm()
    return render(request, 'profile.html', {'form': form})


def upload(request):
    form = UploadForm
    return render(request, 'upload.html', {'form': form})


def signup_user(request):
    form = SignUpForm()
    
    if request.method == "POST":
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, f'Account created successfully')
            return redirect('login')
        
        
    return render(request, 'signup.html', {'form': form})


def login_user(request):
    form = LoginUserForm()
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password1')
        
        user  = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('profile')
            
    return render(request, 'login.html', {'form': form})
