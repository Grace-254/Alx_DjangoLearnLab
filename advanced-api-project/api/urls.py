from django.urls import path

from .views import BookListView, BookDetailView

urlpatterns = [
    # Step 4: BookListView with filtering/search/ordering at /books/
    path("books/", BookListView.as_view(), name="book-list"),

    # Detail/Update/Delete at /books/<pk>/
    path(
        "books/<int:pk>/",
        BookDetailView.as_view(),
        name="book-detail",
    ),
]
