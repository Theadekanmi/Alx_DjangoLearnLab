from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, Permission
from .models import CustomUser, Document


class CustomUserAdmin(UserAdmin):
    """Custom admin for CustomUser."""
    
    list_display = ('email', 'username', 'first_name', 'last_name', 'date_of_birth', 'is_staff')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'date_joined', 'groups')
    
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('email', 'date_of_birth', 'profile_photo')}),
    )
    
    ordering = ('email',)


class DocumentAdmin(admin.ModelAdmin):
    """Admin interface for Document model."""
    list_display = ('title', 'author', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at', 'author')
    search_fields = ('title', 'content')
    readonly_fields = ('created_at', 'updated_at')
    
    def save_model(self, request, obj, form, change):
        if not change:  # If creating new document
            obj.author = request.user
        super().save_model(request, obj, form, change)


# Register models
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Document, DocumentAdmin)

# Customize admin site
admin.site.site_header = "Advanced Features & Security Admin"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome to the Administration Portal"
