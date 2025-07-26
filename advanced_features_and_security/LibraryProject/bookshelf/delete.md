from bookshelf.models import Book

 <!-- Retrieve the book to delete -->
book = Book.objects.get(id=1)
print(f"Book to delete: {book}")

 <!-- Delete the book -->
book.delete()

 <!-- Confirm deletion by trying to retrieve all books -->
all_books = Book.objects.all()
print(f"All books after deletion: {all_books}")

 <!-- Try to retrieve the deleted book (this will raise an exception) -->
try:
    deleted_book = Book.objects.get(id=1)
except Book.DoesNotExist:
    print("Book with ID 1 does not exist - deletion confirmed")