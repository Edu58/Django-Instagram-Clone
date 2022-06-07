from django.contrib.auth.models import User
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
    all_likes = Likes.objects.all()
    return render(request, 'index.html',
                  {'posts': all_posts, 'form': form, 'comments': comments, 'all_users': all_users, 'likes': all_likes})


@login_required(login_url='login')
def profile(request):
    form = ProfileForm()
    
    all_posts = Image.objects.all()

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')

    return render(request, 'profile.html', {'form': form, 'posts': all_posts,})


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


@login_required(login_url='login')
def search(request):
    
    if request.method == "POST":
        term = request.POST.get('term')
        
        image = Image.search_by_name(term)
        
        if image:
            form = CommentForm()
            all_users = Profile.objects.all()
            all_posts = image
            comments = Comments.objects.all()
            return render(request, 'index.html',
                        {'posts': all_posts, 'form': form, 'comments': comments, 'all_users': all_users})
    
    return redirect('home')

@login_required(login_url='login')
def like_image(request,user_id,post_id):
    
    user_voting = User.objects.get(id=user_id)
    image_voted = Image.objects.get(id=post_id)

    new_like = Likes(
        user=user_voting,
        image=image_voted
    )
    new_like.save_like()

    return redirect('home')