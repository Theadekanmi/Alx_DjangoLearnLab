from django.urls import path
from .views import (
    list_books, 
    LibraryDetailView, 
    register_view, 
    CustomLoginView, 
    CustomLogoutView,
    # login_view,
    # logout_view
)

# Define the app namespace
app_name = 'relationship_app'

urlpatterns = [
    # Authentication URLs
    path('register/', register_view, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    
    # Function-based view for listing books
    path('books/', list_books, name='list_books'),
    
    # Class-based view for library details
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    
    # Home page (optional)
    path('', list_books, name='home'),
]