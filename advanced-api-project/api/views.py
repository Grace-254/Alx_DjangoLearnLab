from rest_framework import generics, permissions

from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    """
    ListView: returns all Book instances.

    This view handles read-only access to the collection of books.
    Unauthenticated users can read, but cannot modify any data.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookDetailView(generics.RetrieveAPIView):
    """
    DetailView: returns a single Book instance by primary key.

    This view provides read-only access to one specific book.
    Unauthenticated users can read, but cannot modify any data.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookCreateView(generics.CreateAPIView):
    """
    CreateView: creates new Book instances.

    Only authenticated users are allowed to create new books.
    Incoming data is validated by BookSerializer, including
    custom checks on publication_year.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Hook called after serializer.is_valid() during creation.

        You could attach request.user here if the Book model had
        an owner field. For now we simply save the serializer.
        """
        serializer.save()


class BookUpdateView(generics.UpdateAPIView):
    """
    UpdateView: updates existing Book instances.

    Only authenticated users are allowed to modify books.
    Both full updates (PUT) and partial updates (PATCH) are supported.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        """
        Hook called when a valid update request is processed.

        You can add additional business rules here before saving.
        """
        serializer.save()


class BookDeleteView(generics.DestroyAPIView):
    """
    DeleteView: deletes Book instances.

    Only authenticated users are allowed to delete books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
