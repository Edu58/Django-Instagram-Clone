from re import U
from turtle import pos
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm, LoginUserForm, ProfileForm, UploadForm
from django.contrib import messages
from .models import Image, Profile, Comments, Likes 

# Create your views here.
def home(request):
    all_posts = Image.objects.all()
    print(all_posts)
    return render(request, 'index.html', {'posts': all_posts})


def profile(request):
    form = ProfileForm()
    
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
        
    return render(request, 'profile.html', {'form': form})


def upload(request):
    form = UploadForm()
    current_user = request.user.profile
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.profile = current_user
            post.save()
        return redirect('home')
        
        
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
