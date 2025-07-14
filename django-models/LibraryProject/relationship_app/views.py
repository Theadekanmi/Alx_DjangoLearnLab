from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Book
from .models import Library  
from .models import Author

# Function-based view to list all books
def list_books(request):
    """
    Function-based view that displays all books in the database.
    Returns a simple text list of book titles and their authors.
    """
    books = Book.objects.all()
    
    # Option 1: Simple text response
    if request.GET.get('format') == 'text':
        book_list = []
        for book in books:
            book_list.append(f"{book.title} by {book.author.name}")
        return HttpResponse("\n".join(book_list))
    
    # Option 2: Render with template (recommended)
    context = {
        'books': books
    }
    return render(request, 'relationship_app/list_books.html', context)

# Class-based view to display library details
class LibraryDetailView(DetailView):
    """
    Class-based view that displays details for a specific library,
    including all books available in that library.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add additional context if needed
        context['total_books'] = self.object.books.count()
        return context

# Alternative function-based view for library details (for comparison)
def library_detail_function(request, pk):
    """
    Alternative function-based approach for library details.
    This is for demonstration purposes - you can use either approach.
    """
    library = get_object_or_404(Library, pk=pk)
    context = {
        'library': library,
        'total_books': library.books.count()
    }
    return render(request, 'relationship_app/library_detail.html', context)

# Additional views for enhanced functionality
class BookListView(ListView):
    """
    Class-based ListView alternative for listing books.
    This demonstrates different ways to achieve the same goal.
    """
    model = Book
    template_name = 'relationship_app/book_list.html'
    context_object_name = 'books'
    paginate_by = 10  # Optional pagination
    
    def get_queryset(self):
        # You can customize the queryset here
        return Book.objects.select_related('author').all()

def author_books(request, author_id):
    """
    Function-based view to display books by a specific author.
    """
    author = get_object_or_404(Author, pk=author_id)
    books = Book.objects.filter(author=author)
    
    context = {
        'author': author,
        'books': books
    }
    return render(request, 'relationship_app/author_books.html', context)