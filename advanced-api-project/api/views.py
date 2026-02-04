from rest_framework import generics, permissions

from .models import Book
from .serializers import BookSerializer


class BookListCreateAPIView(generics.ListCreateAPIView):
    """
    ListView + CreateView combined for the Book model.

    - GET /books/  returns all books (read-only, allowed for everyone).
    - POST /books/ creates a new book (write, allowed for authenticated users only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Read-only access for unauthenticated users, write access for authenticated users
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """
        Customize how new Book instances are created.

        This hook is called after serializer.is_valid().
        You can attach request.user here if the Book model had an owner field.
        For now we simply save the serializer.
        """
        serializer.save()


class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    DetailView + UpdateView + DeleteView combined for the Book model.

    - GET    /books/<pk>/ returns details of a specific book (read-only for everyone).
    - PUT    /books/<pk>/ fully updates a book (authenticated users only).
    - PATCH  /books/<pk>/ partially updates a book (authenticated users only).
    - DELETE /books/<pk>/ deletes a book (authenticated users only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Same permission policy: read for everyone, write for authenticated users
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        """
        Customize how existing Book instances are updated.

        Called when a PUT/PATCH request with valid data is made.
        You can add extra logic here before saving.
        """
        serializer.save()
