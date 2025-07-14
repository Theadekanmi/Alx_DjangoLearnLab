from bookshelf.models import Book

 <!-- Retrieve the book to update -->
book = Book.objects.get(id=1)

 <!-- Display current title -->
print(f"Current title: {book.title}")

 <!-- Update the title -->
book.title = "Nineteen Eighty-Four"
book.save()

 <!-- Verify the update -->
print(f"Updated title: {book.title}")