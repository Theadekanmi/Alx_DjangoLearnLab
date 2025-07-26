from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Document


class CustomUserCreationForm(UserCreationForm):
    """Custom user creation form that includes our additional fields."""
    
    email = forms.EmailField(
        required=True,
        help_text='Required. Enter a valid email address.'
    )
    
    date_of_birth = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'}),
        help_text='Optional. Enter your date of birth.'
    )
    
    profile_photo = forms.ImageField(
        required=False,
        help_text='Optional. Upload a profile photo.'
    )
    
    class Meta:
        model = CustomUser
        fields = (
            'username', 'email', 'first_name', 'last_name',
            'date_of_birth', 'profile_photo',
            'password1', 'password2'
        )
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class DocumentForm(forms.ModelForm):
    """Form for creating and editing documents."""
    
    class Meta:
        model = Document
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
