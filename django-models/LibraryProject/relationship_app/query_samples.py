# relationship_app/query_samples.py
"""
Sample queries demonstrating Django ORM relationships.
Run this script from Django shell: python manage.py shell
Then execute: exec(open('relationship_app/query_samples.py').read())
"""

from relationship_app.models import Author, Book, Library, Librarian

def setup_sample_data():
    """
    Create sample data for testing queries.
    """
    # Create authors
    author1 = Author.objects.create(name="J.K. Rowling")
    author2 = Author.objects.create(name="George Orwell")
    author3 = Author.objects.create(name="Harper Lee")
    
    # Create books
    book1 = Book.objects.create(title="Harry Potter and the Philosopher's Stone", author=author1)
    book2 = Book.objects.create(title="Harry Potter and the Chamber of Secrets", author=author1)
    book3 = Book.objects.create(title="1984", author=author2)
    book4 = Book.objects.create(title="Animal Farm", author=author2)
    book5 = Book.objects.create(title="To Kill a Mockingbird", author=author3)
    
    # Create libraries
    library1 = Library.objects.create(name="Central Library")
    library2 = Library.objects.create(name="University Library")
    
    # Add books to libraries (ManyToMany relationship)
    library1.books.add(book1, book2, book3)
    library2.books.add(book3, book4, book5)
    
    # Create librarians
    librarian1 = Librarian.objects.create(name="Alice Johnson", library=library1)
    librarian2 = Librarian.objects.create(name="Bob Smith", library=library2)
    
    print("Sample data created successfully!")

def query_books_by_author():
    """
    Query all books by a specific author.
    Demonstrates ForeignKey relationship usage.
    """
    print("\n=== Query: All books by a specific author ===")
    
    # Method 1: Using filter with author object
    author = Author.objects.get(name="J.K. Rowling")
    books = Book.objects.filter(author=author)
    print(f"Books by {author.name}:")
    for book in books:
        print(f"  - {book.title}")
    
    # Method 2: Using filter with author name (lookup across relationship)
    books = Book.objects.filter(author__name="George Orwell")
    print(f"\nBooks by George Orwell:")
    for book in books:
        print(f"  - {book.title}")
    
    # Method 3: Using reverse relationship
    author = Author.objects.get(name="Harper Lee")
    books = author.book_set.all()
    print(f"\nBooks by {author.name} (using reverse relationship):")
    for book in books:
        print(f"  - {book.title}")

def query_books_in_library():
    """
    List all books in a library.
    Demonstrates ManyToMany relationship usage.
    """
    print("\n=== Query: All books in a library ===")
    
    # Method 1: Using the ManyToMany field directly
    library = Library.objects.get(name="Central Library")
    books = library.books.all()
    print(f"Books in {library.name}:")
    for book in books:
        print(f"  - {book.title} by {book.author.name}")
    
    # Method 2: Using reverse relationship with filter
    books = Book.objects.filter(library__name="University Library")
    print(f"\nBooks in University Library:")
    for book in books:
        print(f"  - {book.title} by {book.author.name}")
    
    # Method 3: Get all libraries and their books
    print(f"\nAll libraries and their books:")
    for library in Library.objects.all():
        print(f"{library.name}:")
        for book in library.books.all():
            print(f"  - {book.title}")

def query_librarian_for_library():
    """
    Retrieve the librarian for a library.
    Demonstrates OneToOne relationship usage.
    """
    print("\n=== Query: Librarian for a library ===")
    
    # Method 1: Using the OneToOne field directly
    library = Library.objects.get(name="Central Library")
    librarian = library.librarian
    print(f"Librarian for {library.name}: {librarian.name}")
    
    # Method 2: Using reverse relationship
    librarian = Librarian.objects.get(library__name="University Library")
    print(f"Librarian for University Library: {librarian.name}")
    
    # Method 3: Get all librarians and their libraries
    print(f"\nAll librarians and their libraries:")
    for librarian in Librarian.objects.all():
        print(f"{librarian.name} manages {librarian.library.name}")

def advanced_queries():
    """
    Additional advanced queries demonstrating complex relationships.
    """
    print("\n=== Advanced Queries ===")
    
    # Query 1: Find all authors who have books in a specific library
    library_name = "Central Library"
    authors = Author.objects.filter(book__library__name=library_name).distinct()
    print(f"Authors with books in {library_name}:")
    for author in authors:
        print(f"  - {author.name}")
    
    # Query 2: Find all libraries that have books by a specific author
    author_name = "George Orwell"
    libraries = Library.objects.filter(books__author__name=author_name).distinct()
    print(f"\nLibraries with books by {author_name}:")
    for library in libraries:
        print(f"  - {library.name}")
    
    # Query 3: Count books per library
    print(f"\nBook count per library:")
    for library in Library.objects.all():
        book_count = library.books.count()
        print(f"  - {library.name}: {book_count} books")
    
    # Query 4: Find libraries managed by librarians whose name contains "Alice"
    libraries = Library.objects.filter(librarian__name__icontains="Alice")
    print(f"\nLibraries managed by librarians with 'Alice' in name:")
    for library in libraries:
        print(f"  - {library.name} (managed by {library.librarian.name})")

def run_all_queries():
    """
    Run all sample queries.
    """
    print("Starting Django ORM Relationship Queries...")
    
    # Create sample data if it doesn't exist
    if not Author.objects.exists():
        setup_sample_data()
    
    # Run all queries
    query_books_by_author()
    query_books_in_library()
    query_librarian_for_library()
    advanced_queries()
    
    print("\n=== All queries completed successfully! ===")

# Run the queries when script is executed
if __name__ == "__main__":
    run_all_queries()