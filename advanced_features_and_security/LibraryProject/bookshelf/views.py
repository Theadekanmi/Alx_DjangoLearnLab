from django.shortcuts import render
from django.http import HttpResponse
from .forms import ExampleForm
from .models import Book

def index(request):
    """Main index view that displays books"""
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

def example_view(request):
    """Example view demonstrating ExampleForm usage"""
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the valid form
            example_data = form.cleaned_data['example_field']
            # You could save to database or process data here
            return render(request, 'bookshelf/form_example.html', {
                'form': ExampleForm(),  # Reset form
                'success_message': f'Form submitted successfully with data: {example_data}'
            })
    else:
        form = ExampleForm()
    
    return render(request, 'bookshelf/form_example.html', {'form': form})
