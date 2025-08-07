from django.db import models

# Create your models here.

class Author(models.Model):
    """
    Author model represents a book author.
    
    This model stores basic information about authors including their name.
    Authors can have multiple books (one-to-many relationship).
    """
    name = models.CharField(max_length=200, help_text="The name of the author")
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


class Book(models.Model):
    """
    Book model represents a book with its publication details.
    
    This model stores information about books including title, publication year,
    and a foreign key relationship to the Author model.
    """
    title = models.CharField(max_length=200, help_text="The title of the book")
    publication_year = models.IntegerField(help_text="The year the book was published")
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE, 
        related_name='books',
        help_text="The author of the book"
    )
    
    def __str__(self):
        return f"{self.title} by {self.author.name}"
    
    class Meta:
        ordering = ['title']
