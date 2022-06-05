from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm, LoginUserForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'index.html')


def profile(request):
    return render(request, 'profile.html')


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
            return redirect('home')
            
    return render(request, 'login.html', {'form': form})
