from django.shortcuts import render, redirect
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.hashers import make_password  # Import this for password hashing
from django.contrib.auth.models import User
from .models import ManifestUser
from django.contrib import messages
from .forms import SignUpForm
def home(request):
    return render(request, 'home.html')

def login_view(request):         
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful. Welcome back!")
            return redirect('base')  # Ensure 'base' is mapped in your urls.py
        else:
            messages.error(request, "Invalid username or password. Please try again.")
    return render(request, 'login.html', {'form': form})
    
def signup(request):
    form = SignUpForm()
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']

            # Check if the user already exists
            if User.objects.filter(username=email).exists():
                messages.error(request, "A user with this email already exists.")
                return render(request, 'signup.html', {'form': form})

            try:
                # Create user in Django auth system
                user = User.objects.create_user(username=email, password=password)
                
                # Save to ManifestUser model
                ManifestUser.objects.create(
                    name=name, 
                    email=email, 
                    password=make_password(password)  # Hashing password for security
                )

                messages.success(request, "Account created successfully. Please log in.")
                print("Account created successfully")
                return redirect('login')

            except IntegrityError:
                messages.error(request, "An error occurred. This email may already be registered.")
    
    return render(request, 'signup.html', {'form': form})



def base(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'base.html')

def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('login')
