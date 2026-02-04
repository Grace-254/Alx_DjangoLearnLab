from django.urls import path

from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    # ListView: read-only list of all books
    path("books/", BookListView.as_view(), name="book-list"),

    # DetailView: read-only details of a single book
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),

    # CreateView: create a new book (authenticated users only)
    path("books/create/", BookCreateView.as_view(), name="book-create"),

    # UpdateView: update an existing book (authenticated users only)
    path("books/<int:pk>/update/", BookUpdateView.as_view(), name="book-update"),

    # DeleteView: delete a book (authenticated users only)
    path("books/<int:pk>/delete/", BookDeleteView.as_view(), name="book-delete"),
]
