from bookshelf.models import Book

<!-- Create a new Book instance -->
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()

<!-- Verify the creation -->
print(f"Book created: {book}")
print(f"Book ID: {book.id}")