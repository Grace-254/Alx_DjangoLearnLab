from django.urls import path
from .views import list_books
from . import views

urlpatterns = [
    path("books/", list_books, name="list_books"),
    path("libraries/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),
]
