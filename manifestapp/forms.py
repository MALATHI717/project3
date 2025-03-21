from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import ManifestUser

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = ManifestUser
        fields = ["name", "email","password"]

