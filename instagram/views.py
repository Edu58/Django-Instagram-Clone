from django.shortcuts import get_object_or_404, redirect, render
from .forms import SignUpForm, LoginUserForm, ProfileForm, UploadForm, CommentForm
from django.contrib import messages
from .models import Image, Profile, Comments, Likes
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def home(request):
    form = CommentForm()
    all_users = Profile.objects.all()
    all_posts = Image.objects.all()
    comments = Comments.objects.all()
    return render(request, 'index.html', {'posts': all_posts, 'form': form, 'comments': comments, 'users': all_users})


@login_required(login_url='login')
def profile(request):
    form = ProfileForm()

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')

    return render(request, 'profile.html', {'form': form})


@login_required(login_url='login')
def comment(request, image_id):
    form = CommentForm()
    current_user = request.user.profile
    image = Image.objects.get(id=image_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.profile = current_user
            comment.image = image
            comment.save()
        return redirect('home')

    return render(request, 'index.html', {'form': form})


@login_required(login_url='login')
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

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')

    return render(request, 'login.html', {'form': form})


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('login')
