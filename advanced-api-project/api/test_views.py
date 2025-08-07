from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Author, Book


class BookAPITestCase(APITestCase):
    """
    Test case for Book API endpoints.
    
    Tests CRUD operations, filtering, searching, ordering, and authentication
    for the Book model API endpoints.
    """
    
    def setUp(self):
        """
        Set up test data and authentication.
        """
        # Create test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
        # Create test author
        self.author = Author.objects.create(name="J.K. Rowling")
        
        # Create test books
        self.book1 = Book.objects.create(
            title="Harry Potter and the Philosopher's Stone",
            publication_year=1997,
            author=self.author
        )
        self.book2 = Book.objects.create(
            title="Harry Potter and the Chamber of Secrets",
            publication_year=1998,
            author=self.author
        )
        
        # Create another author and book for testing
        self.author2 = Author.objects.create(name="George R.R. Martin")
        self.book3 = Book.objects.create(
            title="A Game of Thrones",
            publication_year=1996,
            author=self.author2
        )
        
        # Set up API client
        self.client = APIClient()
    
    def test_list_books_unauthorized(self):
        """
        Test that unauthenticated users can list books.
        """
        url = reverse('api:book-list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 3)
    
    def test_create_book_unauthorized(self):
        """
        Test that unauthenticated users cannot create books.
        """
        url = reverse('api:book-list')
        data = {
            'title': 'New Book',
            'publication_year': 2020,
            'author': self.author.id
        }
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_create_book_authorized(self):
        """
        Test that authenticated users can create books.
        """
        self.client.force_authenticate(user=self.user)
        url = reverse('api:book-list')
        data = {
            'title': 'New Book',
            'publication_year': 2020,
            'author': self.author.id
        }
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)
        self.assertEqual(response.data['title'], 'New Book')
    
    def test_create_book_future_year_validation(self):
        """
        Test that books cannot be created with future publication years.
        """
        self.client.force_authenticate(user=self.user)
        url = reverse('api:book-list')
        data = {
            'title': 'Future Book',
            'publication_year': 2030,
            'author': self.author.id
        }
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('publication_year', response.data)
    
    def test_retrieve_book(self):
        """
        Test retrieving a specific book.
        """
        url = reverse('api:book-detail', args=[self.book1.id])
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)
        self.assertEqual(response.data['publication_year'], self.book1.publication_year)
    
    def test_update_book_unauthorized(self):
        """
        Test that unauthenticated users cannot update books.
        """
        url = reverse('api:book-detail', args=[self.book1.id])
        data = {'title': 'Updated Title'}
        response = self.client.put(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_update_book_authorized(self):
        """
        Test that authenticated users can update books.
        """
        self.client.force_authenticate(user=self.user)
        url = reverse('api:book-detail', args=[self.book1.id])
        data = {
            'title': 'Updated Title',
            'publication_year': 1997,
            'author': self.author.id
        }
        response = self.client.put(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Title')
    
    def test_delete_book_unauthorized(self):
        """
        Test that unauthenticated users cannot delete books.
        """
        url = reverse('api:book-detail', args=[self.book1.id])
        response = self.client.delete(url)
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_delete_book_authorized(self):
        """
        Test that authenticated users can delete books.
        """
        self.client.force_authenticate(user=self.user)
        url = reverse('api:book-detail', args=[self.book1.id])
        response = self.client.delete(url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 2)
    
    def test_filter_books_by_title(self):
        """
        Test filtering books by title.
        """
        url = reverse('api:book-list')
        response = self.client.get(url, {'title': 'Harry Potter'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)
    
    def test_filter_books_by_author(self):
        """
        Test filtering books by author.
        """
        url = reverse('api:book-list')
        response = self.client.get(url, {'author': self.author.id})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)
    
    def test_filter_books_by_publication_year(self):
        """
        Test filtering books by publication year.
        """
        url = reverse('api:book-list')
        response = self.client.get(url, {'publication_year': 1997})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
    
    def test_search_books(self):
        """
        Test searching books by title and author name.
        """
        url = reverse('api:book-list')
        response = self.client.get(url, {'search': 'Harry'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)
    
    def test_order_books_by_title(self):
        """
        Test ordering books by title.
        """
        url = reverse('api:book-list')
        response = self.client.get(url, {'ordering': 'title'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.data['results']
        self.assertEqual(results[0]['title'], 'A Game of Thrones')
        self.assertEqual(results[1]['title'], "Harry Potter and the Chamber of Secrets")
    
    def test_order_books_by_publication_year_desc(self):
        """
        Test ordering books by publication year in descending order.
        """
        url = reverse('api:book-list')
        response = self.client.get(url, {'ordering': '-publication_year'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.data['results']
        self.assertEqual(results[0]['publication_year'], 1998)
        self.assertEqual(results[1]['publication_year'], 1997)
    
    def test_order_books_by_author_name(self):
        """
        Test ordering books by author name.
        """
        url = reverse('api:book-list')
        response = self.client.get(url, {'ordering': 'author__name'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.data['results']
        # George R.R. Martin should come before J.K. Rowling alphabetically
        self.assertEqual(results[0]['author'], self.author2.id)


class AuthorAPITestCase(APITestCase):
    """
    Test case for Author API endpoints.
    
    Tests CRUD operations, searching, ordering, and authentication
    for the Author model API endpoints.
    """
    
    def setUp(self):
        """
        Set up test data and authentication.
        """
        # Create test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
        # Create test authors
        self.author1 = Author.objects.create(name="J.K. Rowling")
        self.author2 = Author.objects.create(name="George R.R. Martin")
        self.author3 = Author.objects.create(name="Stephen King")
        
        # Create test books
        self.book1 = Book.objects.create(
            title="Harry Potter",
            publication_year=1997,
            author=self.author1
        )
        self.book2 = Book.objects.create(
            title="A Game of Thrones",
            publication_year=1996,
            author=self.author2
        )
        
        # Set up API client
        self.client = APIClient()
    
    def test_list_authors_unauthorized(self):
        """
        Test that unauthenticated users can list authors.
        """
        url = reverse('api:author-list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 3)
    
    def test_create_author_unauthorized(self):
        """
        Test that unauthenticated users cannot create authors.
        """
        url = reverse('api:author-list')
        data = {'name': 'New Author'}
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_create_author_authorized(self):
        """
        Test that authenticated users can create authors.
        """
        self.client.force_authenticate(user=self.user)
        url = reverse('api:author-list')
        data = {'name': 'New Author'}
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.count(), 4)
        self.assertEqual(response.data['name'], 'New Author')
    
    def test_retrieve_author_with_books(self):
        """
        Test retrieving a specific author with nested books.
        """
        url = reverse('api:author-detail', args=[self.author1.id])
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.author1.name)
        self.assertEqual(len(response.data['books']), 1)
        self.assertEqual(response.data['books'][0]['title'], 'Harry Potter')
    
    def test_update_author_unauthorized(self):
        """
        Test that unauthenticated users cannot update authors.
        """
        url = reverse('api:author-detail', args=[self.author1.id])
        data = {'name': 'Updated Author'}
        response = self.client.put(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_update_author_authorized(self):
        """
        Test that authenticated users can update authors.
        """
        self.client.force_authenticate(user=self.user)
        url = reverse('api:author-detail', args=[self.author1.id])
        data = {'name': 'Updated Author'}
        response = self.client.put(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.author1.refresh_from_db()
        self.assertEqual(self.author1.name, 'Updated Author')
    
    def test_delete_author_unauthorized(self):
        """
        Test that unauthenticated users cannot delete authors.
        """
        url = reverse('api:author-detail', args=[self.author1.id])
        response = self.client.delete(url)
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_delete_author_authorized(self):
        """
        Test that authenticated users can delete authors.
        """
        self.client.force_authenticate(user=self.user)
        url = reverse('api:author-detail', args=[self.author1.id])
        response = self.client.delete(url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Author.objects.count(), 2)
    
    def test_search_authors(self):
        """
        Test searching authors by name.
        """
        url = reverse('api:author-list')
        response = self.client.get(url, {'search': 'King'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['name'], 'Stephen King')
    
    def test_order_authors_by_name(self):
        """
        Test ordering authors by name.
        """
        url = reverse('api:author-list')
        response = self.client.get(url, {'ordering': 'name'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.data['results']
        self.assertEqual(results[0]['name'], 'George R.R. Martin')
        self.assertEqual(results[1]['name'], 'J.K. Rowling')
        self.assertEqual(results[2]['name'], 'Stephen King')
    
    def test_order_authors_by_name_desc(self):
        """
        Test ordering authors by name in descending order.
        """
        url = reverse('api:author-list')
        response = self.client.get(url, {'ordering': '-name'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.data['results']
        self.assertEqual(results[0]['name'], 'Stephen King')
        self.assertEqual(results[1]['name'], 'J.K. Rowling')
        self.assertEqual(results[2]['name'], 'George R.R. Martin')


class SerializerTestCase(TestCase):
    """
    Test case for custom serializers.
    
    Tests serialization, deserialization, and validation logic.
    """
    
    def setUp(self):
        """
        Set up test data.
        """
        self.author = Author.objects.create(name="Test Author")
        self.book = Book.objects.create(
            title="Test Book",
            publication_year=2020,
            author=self.author
        )
    
    def test_book_serializer_validation_future_year(self):
        """
        Test that BookSerializer rejects future publication years.
        """
        from .serializers import BookSerializer
        
        data = {
            'title': 'Future Book',
            'publication_year': 2030,
            'author': self.author.id
        }
        serializer = BookSerializer(data=data)
        
        self.assertFalse(serializer.is_valid())
        self.assertIn('publication_year', serializer.errors)
    
    def test_book_serializer_validation_valid_year(self):
        """
        Test that BookSerializer accepts valid publication years.
        """
        from .serializers import BookSerializer
        
        data = {
            'title': 'Valid Book',
            'publication_year': 2020,
            'author': self.author.id
        }
        serializer = BookSerializer(data=data)
        
        self.assertTrue(serializer.is_valid())
    
    def test_author_serializer_with_nested_books(self):
        """
        Test that AuthorSerializer includes nested books.
        """
        from .serializers import AuthorSerializer
        
        serializer = AuthorSerializer(self.author)
        data = serializer.data
        
        self.assertIn('books', data)
        self.assertEqual(len(data['books']), 1)
        self.assertEqual(data['books'][0]['title'], 'Test Book')