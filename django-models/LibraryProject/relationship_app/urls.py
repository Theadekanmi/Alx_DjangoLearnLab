from django.urls import path
from . import views

# Define the app namespace
app_name = 'relationship_app'

urlpatterns = [
    # Function-based view for listing books
    path('books/', views.list_books, name='list_books'),
    
    # Class-based view for library details
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    
    # Alternative function-based view for library details (optional)
    path('library/function/<int:pk>/', views.library_detail_function, name='library_detail_function'),
    
    # Additional class-based view for books (alternative approach)
    path('books/class/', views.BookListView.as_view(), name='book_list_class'),
    
    # View for books by specific author
    path('author/<int:author_id>/books/', views.author_books, name='author_books'),
    
    # Home page (optional)
    path('', views.list_books, name='home'),
]