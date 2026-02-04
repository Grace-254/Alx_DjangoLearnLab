from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, filters

from .models import Book
from .serializers import BookSerializer


class BookListCreateAPIView(generics.ListCreateAPIView):
    """
    ListView + CreateView combined for the Book model.

    Supports:
    - Filtering by title, author, and publication_year via query params.
    - Searching by title and author name.
    - Ordering by title and publication_year.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Enable filtering, search, and ordering for this view
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    # Filter by model fields
    filterset_fields = ["title", "author", "publication_year"]
    # Search in these fields (author is a FK, so use name)
    search_fields = ["title", "author__name"]
    # Allow ordering by these fields; ?ordering=-title etc.
    ordering_fields = ["title", "publication_year"]
    # Default ordering if none is specified
    ordering = ["title"]

    def perform_create(self, serializer):
        """
        Customize how new Book instances are created.

        This hook is called after serializer.is_valid().
        """
        serializer.save()


class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    DetailView + UpdateView + DeleteView combined for the Book model.

    - GET    /books/<pk>/ returns details of a specific book.
    - PUT    /books/<pk>/ fully updates a book (authenticated only).
    - PATCH  /books/<pk>/ partially updates a book (authenticated only).
    - DELETE /books/<pk>/ deletes a book (authenticated only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        """
        Customize how existing Book instances are updated.
        """
        serializer.save()
