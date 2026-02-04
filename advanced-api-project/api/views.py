from rest_framework import generics, permissions

from .models import Book
from .serializers import BookSerializer


class BookListCreateAPIView(generics.ListCreateAPIView):
    """
    Handles listing all Book instances and creating new books.

    GET  /api/books/   -> returns a list of all books.
    POST /api/books/   -> creates a new book after validating data
                          with BookSerializer, including the custom
                          publication_year validation.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Allow read-only for unauthenticated users, write for authenticated users
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """
        Customize how new Book instances are created.

        This hook is called after serializer.is_valid(). You can
        attach request.user here if the Book model had an owner
        field. For now we simply save the serializer.
        """
        serializer.save()


class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles retrieve, update, and delete operations for a single Book.

    GET    /api/books/<pk>/ -> returns details of a single book.
    PUT    /api/books/<pk>/ -> fully updates a book instance.
    PATCH  /api/books/<pk>/ -> partially updates a book instance.
    DELETE /api/books/<pk>/ -> deletes the specified book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Same permission: read for everyone, write for authenticated users
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        """
        Customize how existing Book instances are updated.

        Called when a PUT/PATCH request with valid data is made.
        You can add extra logic here, such as logging or enforcing
        additional business rules before saving.
        """
        serializer.save()
