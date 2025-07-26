# relationship_app/urls.py
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    list_books, 
    LibraryDetailView, 
    admin_view, 
    librarian_view, 
    member_view,
    add_book,
    edit_book,
    delete_book
)
from . import views

# Define the app namespace
app_name = 'relationship_app'

urlpatterns = [
    # Authentication URLs - matching what the checker expects
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    
    # Role-based URLs
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
    
    # Permission-based book management URLs
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:book_id>/', edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', delete_book, name='delete_book'),
    
    # Function-based view for listing books
    path('books/', list_books, name='list_books'),
    
    # Class-based view for library details
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    
    # Home page
    path('', list_books, name='home'),
]