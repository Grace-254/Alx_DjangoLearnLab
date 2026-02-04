from django.db import models


class Author(models.Model):
    """
    Represents a book author in the system.

    Each Author can be linked to many Book instances through
    the reverse relationship defined on the Book model.
    """
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    """
    Represents a single book written by an Author.

    The `author` field creates a one-to-many relationship where
    one Author can own many Book records. This is implemented
    via a ForeignKey from Book to Author.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="books",  # lets us access author.books in serializers
    )

    def __str__(self) -> str:
        return f"{self.title} ({self.publication_year})"
