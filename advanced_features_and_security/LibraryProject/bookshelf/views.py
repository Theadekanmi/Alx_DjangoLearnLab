from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ValidationError
from django.db.models import Q
import bleach  # For HTML sanitization - install with: pip install bleach
from .models import Book, Author
from .forms import BookForm

# Permission-protected views for Book model with security enhancements

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    """
    View to list all books - requires 'can_view' permission
    Includes secure search functionality
    """
    books = Book.objects.all()
    
    # Secure search implementation
    search_query = request.GET.get('search', '').strip()
    if search_query:
        # Sanitize search input to prevent XSS
        search_query = bleach.clean(search_query, tags=[], strip=True)
        
        # Use Django ORM for safe parameterized queries (prevents SQL injection)
        books = books.filter(
            Q(title__icontains=search_query) | 
            Q(author__name__icontains=search_query)
        )
    
    return render(request, 'bookshelf/book_list.html', {
        'books': books,
        'search_query': search_query
    })

@permission_required('bookshelf.can_view', raise_exception=True)
def book_detail(request, pk):
    """
    View to display book details - requires 'can_view' permission
    Uses get_object_or_404 for safe object retrieval
    """
    # Safe object retrieval - prevents direct SQL manipulation
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'bookshelf/book_detail.html', {'book': book})

@csrf_protect  # Explicit CSRF protection
@require_http_methods(["GET", "POST"])  # Only allow specific HTTP methods
@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    """
    View to create a new book - requires 'can_create' permission
    Enhanced with input validation and CSRF protection
    """
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            # Additional server-side validation
            try:
                # Form validation already handles basic input sanitization
                book = form.save()
                messages.success(
                    request, 
                    f'Book "{bleach.clean(book.title)}" created successfully!'
                )
                return redirect('book_list')
            except ValidationError as e:
                messages.error(request, f'Validation error: {e}')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = BookForm()
    
    return render(request, 'bookshelf/book_form.html', {
        'form': form, 
        'title': 'Create Book'
    })

@csrf_protect
@require_http_methods(["GET", "POST"])
@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    """
    View to edit an existing book - requires 'can_edit' permission
    Enhanced with input validation and CSRF protection
    """
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            try:
                updated_book = form.save()
                messages.success(
                    request, 
                    f'Book "{bleach.clean(updated_book.title)}" updated successfully!'
                )
                return redirect('book_detail', pk=book.pk)
            except ValidationError as e:
                messages.error(request, f'Validation error: {e}')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = BookForm(instance=book)
    
    return render(request, 'bookshelf/book_form.html', {
        'form': form, 
        'title': 'Edit Book',
        'book': book
    })

@csrf_protect
@require_http_methods(["GET", "POST"])
@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    """
    View to delete a book - requires 'can_delete' permission
    Enhanced with CSRF protection and safe object handling
    """
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == 'POST':
        title = bleach.clean(book.title)  # Sanitize for safe display
        try:
            book.delete()
            messages.success(request, f'Book "{title}" deleted successfully!')
            return redirect('book_list')
        except Exception as e:
            messages.error(request, f'Error deleting book: {e}')
            return redirect('book_detail', pk=pk)
    
    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})

# Alternative approach: Function-based view with manual permission checking
def book_edit_alternative(request, pk):
    """
    Alternative approach to permission checking within the view
    """
    # Check permission manually
    if not request.user.has_perm('bookshelf.can_edit'):
        return HttpResponseForbidden("You don't have permission to edit books.")
    
    book = get_object_or_404(Book, pk=pk)
    # ... rest of the view logic
    pass