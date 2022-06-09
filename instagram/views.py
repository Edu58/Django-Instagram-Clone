from operator import pos
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from .forms import ProfileUpdateForm, SignUpForm, LoginUserForm, ProfileForm, UploadForm, CommentForm, UserUpdateForm
from django.contrib import messages
from django.urls import reverse
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
    return render(request, 'index.html',
                  {'posts': all_posts, 'form': form, 'comments': comments, 'all_users': all_users})


@login_required(login_url='login')
def profile(request):
    all_posts = Image.objects.all()
    return render(request, 'profile.html', {'posts': all_posts,})


@login_required(login_url='login')
def update_profile(request):

    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'prof_form': profile_form
    }

    return render(request, 'update-profile.html', context)


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


@login_required(login_url='login')
def delete_post(request, post_id):
    post = get_object_or_404(Image, pk=post_id)

    if post:
        post.delete()
        return redirect('home')
    
    return redirect('home')


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
            return redirect('home')

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
def like_post(request, post_id):
    post = get_object_or_404(Image, pk=post_id)

    new_like, created = Likes.objects.get_or_create(user=request.user, image=post)

    if not created:
        new_like.delete()

    return redirect(reverse('home'))