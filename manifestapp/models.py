from django.contrib.auth.models import AbstractUser

from django.db import models
from django.contrib.auth.hashers import make_password, is_password_usable
from django.conf import settings

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)  
    def __str__(self):
        return self.username       
    
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username
    
class ManifestLetter(models.Model):
    
    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("scheduled", "Scheduled"),
        ("sent", "Sent"),
        ("failed", "Failed"),
    ]

    id = models.AutoField(primary_key=True)
    user = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_sent = models.BooleanField(default=False)
    scheduled_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default="draft")

    def __str__(self):
        return f"Letter {self.id} - {self.user} - {self.status}"
