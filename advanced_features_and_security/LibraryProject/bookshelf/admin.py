from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    """
    Custom admin interface for the CustomUser model.
    """
    
    # Display configuration
    list_display = (
        'username', 
        'email', 
        'first_name', 
        'last_name', 
        'date_of_birth',
        'profile_photo_preview',
        'is_staff', 
        'is_active'
    )
    
    list_filter = (
        'is_staff', 
        'is_superuser', 
        'is_active', 
        'date_joined',
        'date_of_birth'
    )
    
    search_fields = (
        'username', 
        'first_name', 
        'last_name', 
        'email'
    )
    
    # Fieldsets for the change user form
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': ('date_of_birth', 'profile_photo')
        }),
    )
    
    # Fieldsets for the add user form
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {
            'fields': ('date_of_birth', 'profile_photo')
        }),
    )
    
    def profile_photo_preview(self, obj):
        """Display a small preview of the profile photo in the admin list."""
        if obj.profile_photo:
            return format_html(
                '<img src="{}" width="50" height="50" style="border-radius: 50%;" />',
                obj.profile_photo.url
            )
        return "No Photo"
    profile_photo_preview.short_description = 'Photo'

# Register the custom user admin
admin.site.register(CustomUser, CustomUserAdmin)