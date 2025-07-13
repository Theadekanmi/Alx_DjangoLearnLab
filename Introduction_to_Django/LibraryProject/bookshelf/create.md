cat > bookshelf/create.md << 'EOF'
 <!-- Create Operation -->

 <!-- Command: -->
```python
from bookshelf.models import Book

# Create a new Book instance using Book.objects.create
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Verify the creation
print(f"Book created: {book}")
print(f"Book ID: {book.id}")