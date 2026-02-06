from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet  # Assume you have this

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='books')  # Generates list/create, retrieve/update/delete/ paths

urlpatterns = [
    path('', include(router.urls)),
    # Or explicit function views:
    # path('books/create/', BookCreateView.as_view(), name='book-create'),
    # path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),
    # path('books/delete/<int:pk>/', BookDestroyView.as_view(), name='book-delete'),
]
