from rest_framework import generics, permissions

from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    """
    Read-only view that returns a list of all Book instances.

    GET /books/ -> returns a list of all books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Read-only access is allowed for unauthenticated users
    permission_classes = [permissions.AllowAny]


class BookDetailView(generics.RetrieveAPIView):
    """
    Read-only view that returns a single Book instance by ID.

    GET /books/<pk>/ -> returns details of a single book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookCreateView(generics.CreateAPIView):
    """
    Handles creation of new Book instances.

    POST /books/ -> creates a new book after validating data
                    with BookSerializer (including the
                    publication_year validation).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Only authenticated users can create books
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Hook called after serializer.is_valid() during creation.

        You can attach request.user here if the Book model had an
        owner field. For now, we just save the serializer.
        """
        serializer.save()


class BookUpdateView(generics.UpdateAPIView):
    """
    Handles updating existing Book instances.

    PUT/PATCH /books/<pk>/ -> updates a book instance.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Only authenticated users can update books
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        """
        Hook called when a valid update request is processed.

        You can add extra business rules here before saving.
        """
        serializer.save()


class BookDeleteView(generics.DestroyAPIView):
    """
    Handles deletion of Book instances.

    DELETE /books/<pk>/ -> deletes the specified book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Only authenticated users can delete books
    permission_classes = [permissions.IsAuthenticated]
