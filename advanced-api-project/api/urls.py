from django.urls import path

from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    # ListView: GET /books/
    path("books/", BookListView.as_view(), name="book-list"),

    # CreateView: POST /books/
    path("books/", BookCreateView.as_view(), name="book-create"),

    # DetailView: GET /books/<pk>/
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),

    # UpdateView: PUT/PATCH /books/<pk>/
    path("books/<int:pk>/", BookUpdateView.as_view(), name="book-update"),

    # DeleteView: DELETE /books/<pk>/
    path("books/<int:pk>/", BookDeleteView.as_view(), name="book-delete"),
]
