from rest_framework import serializers
from django.utils import timezone
from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    """
    BookSerializer handles serialization and deserialization of Book model instances.
    
    This serializer includes all fields of the Book model and provides custom validation
    to ensure publication_year is not in the future.
    """
    
    def validate_publication_year(self, value):
        """
        Custom validation to ensure publication_year is not in the future.
        
        Args:
            value: The publication year value to validate
            
        Returns:
            int: The validated publication year
            
        Raises:
            serializers.ValidationError: If the publication year is in the future
        """
        current_year = timezone.now().year
        if value > current_year:
            raise serializers.ValidationError(
                f"Publication year cannot be in the future. Current year is {current_year}."
            )
        return value
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']


class AuthorSerializer(serializers.ModelSerializer):
    """
    AuthorSerializer handles serialization and deserialization of Author model instances.
    
    This serializer includes the author's name field and a nested BookSerializer
    to serialize related books dynamically. The books field is read-only to prevent
    complex nested creation through the author endpoint.
    """
    books = BookSerializer(many=True, read_only=True)
    
    class Meta:
        model = Author
        fields = ['id', 'name', 'books']