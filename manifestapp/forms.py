from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import ManifestUser
from .models import ManifestLetter

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = ManifestUser
        fields = ["name", "email","password"]
class ManifestLetterForm(forms.ModelForm):
    scheduled_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = ManifestLetter
        fields = ["content", "scheduled_date"]  # Fields to be included in the form
        widgets = {
            "scheduled_date": forms.DateInput(attrs={"type": "date"}),  # Date picker
        }