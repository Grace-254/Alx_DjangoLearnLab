from django.urls import path

from .views import (
    BookListCreateAPIView,
    BookRetrieveUpdateDestroyAPIView,
)


urlpatterns = [
    # ListView + CreateView:
    # - GET  /books/  -> list all books
    # - POST /books/  -> create a new book (authenticated only)
    path("books/", BookListCreateAPIView.as_view(), name="book-list-create"),

    # DetailView + UpdateView + DeleteView:
    # - GET    /books/<pk>/ -> retrieve a specific book
    # - PUT    /books/<pk>/ -> update a book (authenticated only)
    # - PATCH  /books/<pk>/ -> partial update (authenticated only)
    # - DELETE /books/<pk>/ -> delete a book (authenticated only)
    path(
        "books/<int:pk>/",
        BookRetrieveUpdateDestroyAPIView.as_view(),
        name="book-detail",
    ),
]
