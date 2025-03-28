from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ManifestLetter, CustomUser


class CustomUserAdmin(UserAdmin):
    # Add 'phone' to the fields displayed in the admin
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Model Iformation', {'fields': ('phone',)}),
    )
    # Add 'phone' to the list display in the admin overview
    list_display = ('username', 'email', 'phone', 'is_staff')


class ManifestLetterAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "status", "created_at", "is_sent", "scheduled_date")
    list_filter = ("status", "is_sent", "created_at")
    search_fields = ("user__email", "content")
    ordering = ("-created_at",)


# Register the models
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(ManifestLetter, ManifestLetterAdmin)