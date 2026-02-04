from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, filters

from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListCreateAPIView):
    """
    ListView + CreateView combined for the Book model.

    This view exposes advanced query capabilities so API consumers can:
    - Filter the book list by title, author, and publication_year using query parameters.
    - Search across book titles and author names for text matches.
    - Order the results by title or publication_year.

    Example requests:
    - /books/?title=Things%20Fall%20Apart
    - /books/?author=1
    - /books/?publication_year=1958
    - /books/?search=Chinua
    - /books/?ordering=title
    - /books/?ordering=-publication_year
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Filtering, searching, and ordering configuration
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    # Step 1: filter by title, author (FK id), and publication_year
    filterset_fields = ["title", "author", "publication_year"]
    # Step 2: search by title and author name
    search_fields = ["title", "author__name"]
    # Step 3: allow ordering by title and publication_year
    ordering_fields = ["title", "publication_year"]
    # Default ordering
    ordering = ["title"]


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
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
