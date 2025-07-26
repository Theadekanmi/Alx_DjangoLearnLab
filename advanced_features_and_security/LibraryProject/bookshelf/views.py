from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from .models import Book, Author
from .forms import BookForm

# Permission-protected views for Book model

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    """
    View to list all books - requires 'can_view' permission
    """
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_view', raise_exception=True)
def book_detail(request, pk):
    """
    View to display book details - requires 'can_view' permission
    """
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'bookshelf/book_detail.html', {'book': book})

@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    """
    View to create a new book - requires 'can_create' permission
    """
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book created successfully!')
            return redirect('book_list')
    else:
        form = BookForm()
    
    return render(request, 'bookshelf/book_form.html', {
        'form': form, 
        'title': 'Create Book'
    })

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    """
    View to edit an existing book - requires 'can_edit' permission
    """
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully!')
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    
    return render(request, 'bookshelf/book_form.html', {
        'form': form, 
        'title': 'Edit Book',
        'book': book
    })

@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    """
    View to delete a book - requires 'can_delete' permission
    """
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == 'POST':
        title = book.title
        book.delete()
        messages.success(request, f'Book "{title}" deleted successfully!')
        return redirect('book_list')
    
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