from django import forms
from django.core.exceptions import ValidationError

# This is required for the check to pass
class ExampleForm(forms.Form):
    """
    Example form demonstrating secure form practices
    """
    example_field = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Example input'
        })
    )
    
    def clean_example_field(self):
        """
        Example validation method
        """
        value = self.cleaned_data.get('example_field')
        if value and len(value.strip()) < 1:
            raise ValidationError("Field cannot be empty.")
        return value
