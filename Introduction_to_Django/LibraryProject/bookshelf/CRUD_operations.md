CRUD Operations Documentation

This document contains all the CRUD operations performed on the Book model using Django's ORM via the Django shell.
Setup
python# Start Django shell
python manage.py shell

 <!-- Import the Book model -->
from bookshelf.models import Book
1. CREATE Operation
Command:
python# Create a new Book instance
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()

 <!-- Verify creation -->
print(f"Book created: {book}")
print(f"Book ID: {book.id}")
Output:
Book created: 1984 by George Orwell
Book ID: 1

2. RETRIEVE Operation
Command:
python# Retrieve the book by ID
book = Book.objects.get(id=1)

# Display all attributes
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")
print(f"ID: {book.id}")
Output:
Title: 1984
Author: George Orwell
Publication Year: 1949
ID: 1
3. UPDATE Operation
Command:
python# Retrieve the book to update
book = Book.objects.get(id=1)
print(f"Current title: {book.title}")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Verify the update
print(f"Updated title: {book.title}")
Output:
Current title: 1984
Updated title: Nineteen Eighty-Four
4. DELETE Operation
Command:
python# Retrieve the book to delete
book = Book.objects.get(id=1)
print(f"Book to delete: {book}")

# Delete the book
book.delete()

# Confirm deletion
all_books = Book.objects.all()
print(f"All books after deletion: {all_books}")

# Verify deletion
try:
    deleted_book = Book.objects.get(id=1)
except Book.DoesNotExist:
    print("Book with ID 1 does not exist - deletion confirmed")
Output:
Book to delete: Nineteen Eighty-Four by George Orwell
All books after deletion: <QuerySet []>
Book with ID 1 does not exist - deletion confirmed
Summary
All CRUD operations have been successfully performed:

✅ Create: Book instance created with title "1984"
✅ Retrieve: Book details retrieved and displayed
✅ Update: Book title updated to "Nineteen Eighty-Four"
✅ Delete: Book instance deleted and deletion confirmed

The Django ORM provides a powerful and intuitive way to interact with the database without writing raw SQL queries.