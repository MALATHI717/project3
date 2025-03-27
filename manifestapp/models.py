from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.hashers import make_password, is_password_usable

# class ManifestUserManager(models.Manager):
#     def create_user(self, email, name, password, **extra_fields):
#         """Creates a new user with a hashed password and a name."""
#         if self.filter(email=email).exists():
#             raise ValueError("User with this email already exists")
        
#         # Hash the password before saving
#         hashed_password = make_password(password)
#         user = self.create(email=email, name=name, password=hashed_password, **extra_fields)
#         return user

#class ManifestUser(models.Model):
    #id = models.AutoField(primary_key=True)
   # name = models.CharField(max_length=255)  # Added name field
   ## password = models.CharField(max_length=255)
    #created_at = models.DateTimeField(auto_now_add=True)
    
   # objects = ManifestUserManager()  # Use the custom manager
# def __str__(self):
       # return self.email

   # def save(self, *args, **kwargs):
        # Ensure the password is hashed before saving
        #if not is_password_usable(self.password):
        #    self.password = make_password(self.password)
       # super().save(*args, **kwargs)
       

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
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="draft")

    def __str__(self):
        return f"Letter {self.id} - {self.user} - {self.status}"
