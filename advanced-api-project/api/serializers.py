from datetime import datetime

from rest_framework import serializers

from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    """
    Serializes and validates Book instances for API input/output.

    This serializer exposes all fields of the Book model and
    adds custom validation to ensure that `publication_year`
    cannot be set in the future.
    """

    class Meta:
        model = Book
        fields = "__all__"

    def validate_publication_year(self, value: int) -> int:
        """
        Ensure that the publication_year is not in the future.

        DRF calls this field-level validator automatically when
        validating the `publication_year` field. If the year is
        greater than the current year, a ValidationError is raised.
        """
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes Author instances along with their related books.

    The nested `books` field uses the BookSerializer with
    many=True to represent the one-to-many relationship
    between Author and Book as a list of nested objects
    in the API response.
    """

    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["id", "name", "books"]
