from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Using Django's built-in User model
from .models import ManifestLetter  # Ensure this model exists

class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=100, required=True, label="Full Name")
    email = forms.EmailField(required=True, label="Email")
    phone = forms.CharField(max_length=10, required=True, label="phone number")

    class Meta:
        model = User
        fields = ["name", "email", "password1", "password2","phone"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this email already exists.")
        return email

class ManifestLetterForm(forms.ModelForm):
    scheduled_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = ManifestLetter
        fields = ["content", "scheduled_date"]  # Fields to be included in the form
        widgets = {
            "scheduled_date": forms.DateInput(attrs={"type": "date"}),  # Date picker
        }
