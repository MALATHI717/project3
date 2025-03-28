from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Using Django's built-in User model
from .models import ManifestLetter  # Ensure this model exists
from .models import customUser  # Import your custom user model

class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=100, required=True, label="Full Name")
    email = forms.EmailField(required=True, label="Email")
    phone = forms.CharField(max_length=15, required=True, label="Phone Number")  # Match max_length with model

    class Meta:
        model = customUser  # Use customUser instead of User
        fields = ["name", "email", "phone", "password1", "password2"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if customUser.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this email already exists.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data["email"]  # Optional: Use email as username
        user.first_name = self.cleaned_data["name"]  # Store full name in first_name
        user.phone = self.cleaned_data["phone"]  # Save phone number
        if commit:
            user.save()
        return user

class ManifestLetterForm(forms.ModelForm):
    scheduled_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = ManifestLetter
        fields = ["content", "scheduled_date"]  # Fields to be included in the form
        widgets = {
            "scheduled_date": forms.DateInput(attrs={"type": "date"}),  # Date picker
        }
