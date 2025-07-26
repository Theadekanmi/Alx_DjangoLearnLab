from django import forms
from .models import Book, Author

class BookForm(forms.ModelForm):
    """
    Form for creating and editing books
    """
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter book title'
            }),
            'author': forms.Select(attrs={
                'class': 'form-control'
            }),
            'publication_year': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter publication year'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ensure all authors are available in the dropdown
        self.fields['author'].queryset = Author.objects.all()
        
        # Add labels
        self.fields['title'].label = 'Book Title'
        self.fields['author'].label = 'Author'
        self.fields['publication_year'].label = 'Publication Year'