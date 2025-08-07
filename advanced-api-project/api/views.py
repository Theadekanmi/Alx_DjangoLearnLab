from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer


class BookListView(generics.ListCreateAPIView):
    """
    ListCreateAPIView for Book model.
    
    Provides GET (list all books) and POST (create new book) operations.
    Includes filtering, searching, and ordering capabilities.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year', 'author__name']
    ordering = ['title']
    
    def get_permissions(self):
        """
        Customize permissions based on the HTTP method.
        - GET: Allow any user (read-only)
        - POST: Require authentication (create)
        """
        if self.request.method == 'GET':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    RetrieveUpdateDestroyAPIView for Book model.
    
    Provides GET (retrieve single book), PUT/PATCH (update book), 
    and DELETE (delete book) operations.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def get_permissions(self):
        """
        Customize permissions based on the HTTP method.
        - GET: Allow any user (read-only)
        - PUT/PATCH/DELETE: Require authentication
        """
        if self.request.method == 'GET':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]


class AuthorListView(generics.ListCreateAPIView):
    """
    ListCreateAPIView for Author model.
    
    Provides GET (list all authors) and POST (create new author) operations.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']
    ordering = ['name']
    
    def get_permissions(self):
        """
        Customize permissions based on the HTTP method.
        - GET: Allow any user (read-only)
        - POST: Require authentication (create)
        """
        if self.request.method == 'GET':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]


class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    RetrieveUpdateDestroyAPIView for Author model.
    
    Provides GET (retrieve single author), PUT/PATCH (update author), 
    and DELETE (delete author) operations.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
    def get_permissions(self):
        """
        Customize permissions based on the HTTP method.
        - GET: Allow any user (read-only)
        - PUT/PATCH/DELETE: Require authentication
        """
        if self.request.method == 'GET':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]
