cat > bookshelf/retrieve.md << 'EOF'
 <!-- Retrieve Operation -->

<!-- Command: -->
```python
from bookshelf.models import Book

# Retrieve the book by ID
book = Book.objects.get(id=1)

# Display all attributes
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")
print(f"ID: {book.id}")