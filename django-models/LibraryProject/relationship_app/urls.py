# relationship_app/urls.py
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    list_books, 
    LibraryDetailView, 
    admin_view, 
    librarian_view, 
    member_view
)
from . import views

# Define the app namespace
app_name = 'relationship_app'

urlpatterns = [
    # Authentication URLs (keeping your existing ones)
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    
    # Role-based access URLs
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
    
    # Main app URLs (keeping your existing ones)
    path('', list_books, name='home'),
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]