from django.urls import path

from .views import (
    BookListCreateAPIView,
    BookRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    # GET /books/ (list), POST /books/ (create)
    path("books/", BookListCreateAPIView.as_view(), name="book-list-create"),

    # GET /books/<pk>/ (detail), PUT/PATCH/DELETE (update/delete)
    path(
        "books/<int:pk>/",
        BookRetrieveUpdateDestroyAPIView.as_view(),
        name="book-detail",
    ),
]
