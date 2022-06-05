from django.shortcuts import render
from .forms import SignUpForm, LoginUserForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'index.html')


def profile(request):
    return render(request, 'profile.html')


def signup(request):
    form = SignUpForm()
    
    if request.method == "POST":
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, f'Account created successfully')
            return redirect('login')
        
        
    return render(request, 'signup.html', {'form': form})


def login(request):
    form = LoginUserForm()
    
    if request.method == "POST":
        form = LoginUserForm(request.POST)
        
        if form.is_valid():
            print(form.username)
            
    return render(request, 'login.html', {'form': form})
