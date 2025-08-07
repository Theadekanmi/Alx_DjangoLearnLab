# Advanced API Development with Django REST Framework

This project demonstrates advanced API development concepts using Django REST Framework, including custom serializers, generic views, filtering, searching, ordering, and comprehensive testing.

## Features

- **Custom Serializers**: Handle complex data structures and nested relationships
- **Generic Views**: Efficient CRUD operations using DRF's generic views
- **Filtering & Searching**: Advanced query capabilities for data retrieval
- **Ordering**: Flexible sorting options
- **Authentication & Permissions**: Secure API endpoints with proper access control
- **Comprehensive Testing**: Unit tests for all API endpoints

## Project Structure

```
advanced-api-project/
├── advanced_api_project/     # Main Django project
├── api/                      # API application
│   ├── models.py            # Author and Book models
│   ├── serializers.py       # Custom serializers
│   ├── views.py             # Generic views
│   ├── urls.py              # API URL patterns
│   └── test_views.py        # Unit tests
├── manage.py
└── README.md
```

## Models

### Author Model
- `name`: CharField - The author's name
- Related books through foreign key relationship

### Book Model
- `title`: CharField - The book's title
- `publication_year`: IntegerField - Year of publication
- `author`: ForeignKey to Author - The book's author

## API Endpoints

### Books
- `GET /api/books/` - List all books (with filtering, searching, ordering)
- `POST /api/books/` - Create a new book (requires authentication)
- `GET /api/books/{id}/` - Retrieve a specific book
- `PUT /api/books/{id}/` - Update a book (requires authentication)
- `PATCH /api/books/{id}/` - Partially update a book (requires authentication)
- `DELETE /api/books/{id}/` - Delete a book (requires authentication)

### Authors
- `GET /api/authors/` - List all authors (with searching, ordering)
- `POST /api/authors/` - Create a new author (requires authentication)
- `GET /api/authors/{id}/` - Retrieve a specific author with nested books
- `PUT /api/authors/{id}/` - Update an author (requires authentication)
- `PATCH /api/authors/{id}/` - Partially update an author (requires authentication)
- `DELETE /api/authors/{id}/` - Delete an author (requires authentication)

## Query Parameters

### Filtering
- `?title=harry` - Filter books by title
- `?author=1` - Filter books by author ID
- `?publication_year=1997` - Filter books by publication year

### Searching
- `?search=harry` - Search in book titles and author names
- `?search=rowling` - Search in author names

### Ordering
- `?ordering=title` - Order by title (ascending)
- `?ordering=-publication_year` - Order by publication year (descending)
- `?ordering=author__name` - Order by author name

## Authentication

The API uses Django REST Framework's built-in authentication:
- **Session Authentication**: For web interface
- **Basic Authentication**: For API clients

### Permissions
- **Read operations** (GET): Available to all users
- **Write operations** (POST, PUT, PATCH, DELETE): Require authentication

## Installation and Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd advanced-api-project
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django djangorestframework django-filter
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

## Testing

Run the test suite:
```bash
python manage.py test api
```

## Usage Examples

### Creating an Author
```bash
curl -X POST http://localhost:8000/api/authors/ \
  -H "Content-Type: application/json" \
  -d '{"name": "J.K. Rowling"}'
```

### Creating a Book
```bash
curl -X POST http://localhost:8000/api/books/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Harry Potter", "publication_year": 1997, "author": 1}'
```

### Filtering Books
```bash
curl "http://localhost:8000/api/books/?publication_year=1997"
```

### Searching Books
```bash
curl "http://localhost:8000/api/books/?search=harry"
```

### Ordering Results
```bash
curl "http://localhost:8000/api/books/?ordering=-publication_year"
```

## Custom Serializers

### BookSerializer
- Serializes all Book model fields
- Includes custom validation for publication_year (cannot be in the future)
- Handles author foreign key relationship

### AuthorSerializer
- Serializes Author model with nested BookSerializer
- Provides read-only access to related books
- Prevents complex nested creation through author endpoint

## View Configuration

### Generic Views Used
- **ListCreateAPIView**: For listing and creating resources
- **RetrieveUpdateDestroyAPIView**: For retrieving, updating, and deleting resources

### Custom Features
- **Dynamic permissions**: Different permissions based on HTTP method
- **Filter backends**: DjangoFilterBackend, SearchFilter, OrderingFilter
- **Custom queryset methods**: Optimized database queries
- **Response customization**: Proper error handling and status codes

## Validation

The BookSerializer includes custom validation:
- Publication year cannot be in the future
- All required fields must be provided
- Author must exist in the database

## Error Handling

The API provides comprehensive error handling:
- **400 Bad Request**: Invalid data or validation errors
- **401 Unauthorized**: Missing or invalid authentication
- **403 Forbidden**: Insufficient permissions
- **404 Not Found**: Resource not found
- **500 Internal Server Error**: Server-side errors

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Run the test suite
6. Submit a pull request

## License

This project is licensed under the MIT License.