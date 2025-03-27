from django.contrib import admin
from .models import ManifestLetter

#@admin.register(ManifestUser)
#class ManifestUserAdmin(admin.ModelAdmin):
    #list_display = ("id", "name", "email", "created_at")
   # search_fields = ("email", "name")
    #ordering = ("-created_at",)

    

@admin.register(ManifestLetter)
class ManifestLetterAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "status", "created_at", "is_sent", "scheduled_date")
    list_filter = ("status", "is_sent", "created_at")
    search_fields = ("user__email", "content")
    ordering = ("-created_at",)
