from django.urls import path

from .views import (
    BookListCreateAPIView,
    BookRetrieveUpdateDestroyAPIView,
)


urlpatterns = [
    # ListView + CreateView combined
    # GET  /api/books/  -> list all books
    # POST /api/books/  -> create a new book
    path("books/", BookListCreateAPIView.as_view(), name="book-list-create"),

    # DetailView + UpdateView + DeleteView combined
    # GET    /api/books/<pk>/ -> retrieve a specific book
    # PUT    /api/books/<pk>/ -> update a book
    # PATCH  /api/books/<pk>/ -> partial update
    # DELETE /api/books/<pk>/ -> delete a book
    path(
        "books/<int:pk>/",
        BookRetrieveUpdateDestroyAPIView.as_view(),
        name="book-detail",
    ),
]
