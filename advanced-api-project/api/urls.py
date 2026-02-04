from django.urls import path

from .views import (
    BookListView,
    BookDetailView,
)

urlpatterns = [
    # GET /books/ (list), POST /books/ (create)
    path("books/", BookListView.as_view(), name="book-list"),

    # GET /books/<pk>/, PUT/PATCH/DELETE /books/<pk>/
    path(
        "books/<int:pk>/",
        BookDetailView.as_view(),
        name="book-detail",
    ),
]
