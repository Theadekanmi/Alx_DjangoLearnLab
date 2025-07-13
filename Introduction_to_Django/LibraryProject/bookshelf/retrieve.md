
```bash
cat > bookshelf/retrieve.md << 'EOF'
# Retrieve Operation

```python
from bookshelf.models import Book

# Retrieve the book by ID
book = Book.objects.get(id=1)

# Display all attributes
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")
print(f"ID: {book.id}")

# Expected Output:
# Title: 1984
# Author: George Orwell
# Publication Year: 1949
# ID: 1