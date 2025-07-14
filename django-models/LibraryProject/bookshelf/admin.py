from django.contrib import admin
from .models import Book

# Register the Book model with custom admin configuration
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Display these fields in the admin list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add filters for these fields in the admin sidebar
    list_filter = ('author', 'publication_year')
    
    # Enable search functionality for these fields
    search_fields = ('title', 'author')
    
    # Optional: Add ordering
    ordering = ('title',)
    
    # Optional: Add fields to display in the detail view
    fields = ('title', 'author', 'publication_year')
    
    # Optional: Customize the number of items per page
    list_per_page = 20