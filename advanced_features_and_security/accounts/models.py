from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.conf import settings


class CustomUserManager(BaseUserManager):
    """Custom manager for CustomUser."""
    
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    """Custom user model with additional fields."""
    
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.email


class Document(models.Model):
    """
    Document model with custom permissions for testing permission system.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        # STEP 1: Define custom permissions
        permissions = [
            ("can_view", "Can view document"),
            ("can_create", "Can create document"),
            ("can_edit", "Can edit document"),
            ("can_delete", "Can delete document"),
        ]
    
    def __str__(self):
        return self.title


# Example of how to reference the custom user model in other models
class UserProfile(models.Model):
    """Example model that references the custom user."""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    
    def __str__(self):
        return f"{self.user.email}'s profile"
