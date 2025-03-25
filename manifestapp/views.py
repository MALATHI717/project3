from django.shortcuts import render, redirect
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.hashers import make_password  # Hash passwords for security
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import ManifestUser, ManifestLetter
from .forms import SignUpForm, ManifestLetterForm
from django.utils.timezone import make_aware
from datetime import datetime

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
            return redirect('base')  # Ensure 'base' is mapped in urls.py
        else:
            messages.error(request, "Invalid username or password. Please try again.")
    
    return render(request, 'login.html', {'form': form})

def signup_view(request):
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
                return redirect('login')

            except IntegrityError:
                messages.error(request, "An error occurred. This email may already be registered.")
    
    return render(request, 'signup.html', {'form': form})

@login_required
def base_view(request):
    if request.method == "POST":
        form = ManifestLetterForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data["content"]
            scheduled_date = form.cleaned_data["scheduled_date"]

            # Ensure scheduled_date is a datetime object, not just a date
            if isinstance(scheduled_date, datetime):
                scheduled_date = make_aware(scheduled_date) # Convert to timezone-aware datetime
            else:
                # Convert date to datetime before making it timezone-aware
                scheduled_date = make_aware(datetime.combine(scheduled_date, datetime.min.time()))

            try:
                manifest_user = ManifestUser.objects.get(email=request.user.username)
            except ManifestUser.DoesNotExist:
                messages.error(request, "User does not exist in ManifestUser.")
                return redirect("signup")

            # Save data in DB
            ManifestLetter.objects.create(
                user=manifest_user,
                content=content,
                scheduled_date=scheduled_date,
                status="draft",
            )

            messages.success(request, "Your letter has been saved as a draft.")
            return redirect("base")
        else:
            messages.error(request, "Please correct the errors in the form.")

    else:
        form = ManifestLetterForm()

    return render(request, "base.html", {"form": form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('login')
