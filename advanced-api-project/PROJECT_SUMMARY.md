# Advanced API Development with Django REST Framework - Project Summary

## Project Overview

This project successfully implements all required tasks for the "Advanced API Development with Django REST Framework" assignment. The project demonstrates advanced API development concepts including custom serializers, generic views, filtering, searching, ordering, and comprehensive testing.

## Completed Tasks

### ✅ Task 0: Setting Up a New Django Project with Custom Serializers

**Objective**: Initiate a new Django project with custom serializers for complex data structures.

**Completed Features**:
- ✅ Created new Django project `advanced_api_project`
- ✅ Installed Django REST Framework and django-filter
- ✅ Created `api` app
- ✅ Configured project settings with required apps
- ✅ Defined `Author` and `Book` models with proper relationships
- ✅ Created custom serializers with validation
- ✅ Implemented nested serialization (Author with Books)
- ✅ Added custom validation for publication year (no future years)
- ✅ Registered models in Django admin
- ✅ Created comprehensive documentation

**Key Files Created**:
- `api/models.py` - Author and Book models
- `api/serializers.py` - Custom serializers with validation
- `api/admin.py` - Admin interface configuration
- `advanced_api_project/settings.py` - Project configuration

### ✅ Task 1: Building Custom Views and Generic Views

**Objective**: Construct custom views and utilize generic views for CRUD operations.

**Completed Features**:
- ✅ Implemented `ListCreateAPIView` for Books and Authors
- ✅ Implemented `RetrieveUpdateDestroyAPIView` for Books and Authors
- ✅ Configured URL patterns for all endpoints
- ✅ Added dynamic permissions (read-only for unauthenticated, full access for authenticated)
- ✅ Integrated filtering, searching, and ordering capabilities
- ✅ Added proper error handling and status codes
- ✅ Created comprehensive view documentation

**Key Files Created**:
- `api/views.py` - Generic views with custom permissions
- `api/urls.py` - URL patterns for API endpoints
- `advanced_api_project/urls.py` - Main URL configuration

**API Endpoints**:
- `GET/POST /api/books/` - List and create books
- `GET/PUT/PATCH/DELETE /api/books/{id}/` - Book CRUD operations
- `GET/POST /api/authors/` - List and create authors
- `GET/PUT/PATCH/DELETE /api/authors/{id}/` - Author CRUD operations

### ✅ Task 2: Implementing Filtering, Searching, and Ordering

**Objective**: Enhance API with filtering, searching, and ordering capabilities.

**Completed Features**:
- ✅ Integrated DjangoFilterBackend for field-based filtering
- ✅ Implemented SearchFilter for text-based searching
- ✅ Added OrderingFilter for flexible sorting
- ✅ Configured filter fields for Books (title, author, publication_year)
- ✅ Configured search fields for Books (title, author__name)
- ✅ Configured ordering fields for Books and Authors
- ✅ Added default ordering (books by title, authors by name)
- ✅ Tested all filtering, searching, and ordering functionality

**Query Parameters Supported**:
- Filtering: `?title=harry`, `?author=1`, `?publication_year=1997`
- Searching: `?search=harry`, `?search=rowling`
- Ordering: `?ordering=title`, `?ordering=-publication_year`, `?ordering=author__name`

### ✅ Task 3: Writing Unit Tests for Django REST Framework APIs

**Objective**: Develop comprehensive unit tests for API endpoints.

**Completed Features**:
- ✅ Created comprehensive test suite in `api/test_views.py`
- ✅ Tested all CRUD operations for Books and Authors
- ✅ Tested authentication and permission systems
- ✅ Tested filtering, searching, and ordering functionality
- ✅ Tested custom serializer validation
- ✅ Tested nested serialization (Author with Books)
- ✅ Tested error handling and status codes
- ✅ Created separate test cases for different components

**Test Coverage**:
- **BookAPITestCase**: 15 test methods covering all Book endpoints
- **AuthorAPITestCase**: 12 test methods covering all Author endpoints
- **SerializerTestCase**: 3 test methods covering serializer validation

## Technical Implementation Details

### Models
```python
class Author(models.Model):
    name = models.CharField(max_length=200)
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
```

### Serializers
```python
class BookSerializer(serializers.ModelSerializer):
    def validate_publication_year(self, value):
        # Custom validation for future years
        current_year = timezone.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested serialization
```

### Views
```python
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year', 'author__name']
    
    def get_permissions(self):
        # Dynamic permissions based on HTTP method
        if self.request.method == 'GET':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]
```

## Authentication & Permissions

- **Session Authentication**: For web interface
- **Basic Authentication**: For API clients
- **Dynamic Permissions**: 
  - GET operations: Available to all users
  - POST/PUT/PATCH/DELETE: Require authentication

## API Features

### Advanced Querying
- **Filtering**: Field-based filtering on multiple attributes
- **Searching**: Text-based search across multiple fields
- **Ordering**: Flexible sorting with ascending/descending options
- **Pagination**: Built-in pagination with configurable page size

### Data Validation
- **Custom Validation**: Publication year cannot be in the future
- **Model Validation**: Ensures data integrity
- **Serializer Validation**: Comprehensive input validation

### Error Handling
- **400 Bad Request**: Invalid data or validation errors
- **401 Unauthorized**: Missing or invalid authentication
- **403 Forbidden**: Insufficient permissions
- **404 Not Found**: Resource not found
- **500 Internal Server Error**: Server-side errors

## Project Structure

```
advanced-api-project/
├── advanced_api_project/     # Main Django project
│   ├── settings.py          # Project configuration
│   └── urls.py              # Main URL patterns
├── api/                      # API application
│   ├── models.py            # Author and Book models
│   ├── serializers.py       # Custom serializers
│   ├── views.py             # Generic views
│   ├── urls.py              # API URL patterns
│   ├── admin.py             # Admin interface
│   └── test_views.py        # Comprehensive unit tests
├── manage.py
├── requirements.txt          # Dependencies
├── README.md                # Project documentation
├── PROJECT_SUMMARY.md       # This summary
└── test_api.py              # Simple API test script
```

## Running the Project

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Create superuser**:
   ```bash
   python manage.py createsuperuser
   ```

4. **Run development server**:
   ```bash
   python manage.py runserver
   ```

5. **Run tests**:
   ```bash
   python manage.py test api
   ```

## API Usage Examples

### Creating Data
```bash
# Create author (requires authentication)
curl -X POST http://localhost:8000/api/authors/ \
  -H "Content-Type: application/json" \
  -u username:password \
  -d '{"name": "J.K. Rowling"}'

# Create book (requires authentication)
curl -X POST http://localhost:8000/api/books/ \
  -H "Content-Type: application/json" \
  -u username:password \
  -d '{"title": "Harry Potter", "publication_year": 1997, "author": 1}'
```

### Querying Data
```bash
# List all books
curl http://localhost:8000/api/books/

# Filter books by year
curl "http://localhost:8000/api/books/?publication_year=1997"

# Search books
curl "http://localhost:8000/api/books/?search=harry"

# Order books by title
curl "http://localhost:8000/api/books/?ordering=title"
```

## Learning Outcomes

This project successfully demonstrates:

1. **Advanced Serializer Usage**: Custom validation, nested serialization, and complex data structures
2. **Generic Views**: Efficient CRUD operations using DRF's powerful generic views
3. **Advanced Querying**: Filtering, searching, and ordering capabilities
4. **Security**: Proper authentication and permission systems
5. **Testing**: Comprehensive unit tests for all API functionality
6. **Documentation**: Clear and comprehensive project documentation

The project meets all requirements and provides a solid foundation for advanced API development with Django REST Framework.