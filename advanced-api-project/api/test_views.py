from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Author, Book
from .serializers import BookSerializer

User = get_user_model()


class BookAPITests(APITestCase):
    """
    Test suite for the Book API endpoints.

    Covers:
    - CRUD operations for Book
    - Filtering, searching, and ordering on the list endpoint
    - Permission behavior for authenticated vs unauthenticated users
    """

    def setUp(self):
        """
        Prepare common test data for all tests.

        Creates one author and three books with different titles and
        publication years, and also creates a regular test user that
        is used for authenticated requests.
        """
        self.author = Author.objects.create(name="Chinua Achebe")

        self.book1 = Book.objects.create(
            title="Things Fall Apart",
            publication_year=1958,
            author=self.author,
        )
        self.book2 = Book.objects.create(
            title="No Longer at Ease",
            publication_year=1960,
            author=self.author,
        )
        self.book3 = Book.objects.create(
            title="Anthills of the Savannah",
            publication_year=1987,
            author=self.author,
        )

        self.user = User.objects.create_user(
            username="testuser", password="testpassword123"
        )

        # Base URLs for the list and detail endpoints
        self.list_url = reverse("book-list")
        self.detail_url = reverse("book-detail", args=[self.book1.pk])

    # --------- CRUD tests ---------

    def test_list_books_anonymous_allowed(self):
        """
        Anonymous users should be able to retrieve the list of books.

        Verifies that GET /books/ returns HTTP 200 and includes
        the serialized data for all existing Book instances.
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Use serializer to compare response data shape
        books = Book.objects.all().order_by("title")
        serializer = BookSerializer(books, many=True)
        # Because ordering is by title by default, we sort queryset similarly
        returned_titles = sorted([b["title"] for b in response.data])
        expected_titles = sorted([b["title"] for b in serializer.data])
        self.assertEqual(returned_titles, expected_titles)

    def test_create_book_requires_authentication(self):
        """
        Anonymous users should NOT be able to create books.

        Verifies that POST /books/ without authentication returns
        HTTP 401 or 403 and does not create a new Book instance.
        """
        payload = {
            "title": "New Book",
            "publication_year": 2000,
            "author": self.author.pk,
        }
        response = self.client.post(self.list_url, payload, format="json")
        self.assertIn(response.status_code, (status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN))
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_authenticated(self):
        """
        Authenticated users should be able to create books.

        Verifies that POST /books/ with valid data and authentication
        returns HTTP 201 and the book is stored in the database.
        """
        self.client.login(username="testuser", password="testpassword123")
        payload = {
            "title": "Arrow of God",
            "publication_year": 1964,
            "author": self.author.pk,
        }
        response = self.client.post(self.list_url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)
        self.assertEqual(Book.objects.latest("id").title, "Arrow of God")

    def test_update_book_authenticated(self):
        """
        Authenticated users should be able to update existing books.

        Verifies that PUT /books/<pk>/ updates the title and returns
        HTTP 200 with the updated data.
        """
        self.client.login(username="testuser", password="testpassword123")
        payload = {
            "title": "Things Fall Apart (Updated)",
            "publication_year": self.book1.publication_year,
            "author": self.author.pk,
        }
        response = self.client.put(self.detail_url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Things Fall Apart (Updated)")

    def test_delete_book_authenticated(self):
        """
        Authenticated users should be able to delete books.

        Verifies that DELETE /books/<pk>/ returns HTTP 204 and the
        Book instance is removed from the database.
        """
        self.client.login(username="testuser", password="testpassword123")
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=self.book1.pk).exists())

    # --------- Filtering, searching, ordering tests ---------

    def test_filter_books_by_title(self):
        """
        Verify that filtering by title returns only matching books.

        Uses /books/?title=Things%20Fall%20Apart to filter the list.
        """
        response = self.client.get(self.list_url, {"title": "Things Fall Apart"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Things Fall Apart")

    def test_filter_books_by_publication_year(self):
        """
        Verify that filtering by publication_year returns the correct set.

        Uses /books/?publication_year=1960 to filter the list.
        """
        response = self.client.get(self.list_url, {"publication_year": 1960})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "No Longer at Ease")

    def test_search_books_by_title(self):
        """
        Verify that search query matches titles containing the term.

        Uses /books/?search=Anthills to search by title.
        """
        response = self.client.get(self.list_url, {"search": "Anthills"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Anthills of the Savannah")

    def test_search_books_by_author_name(self):
        """
        Verify that search across author name returns all books by that author.

        Uses /books/?search=Chinua to search by author__name.
        """
        response = self.client.get(self.list_url, {"search": "Chinua"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # All three books share the same author
        self.assertEqual(len(response.data), 3)

    def test_order_books_by_title(self):
        """
        Verify that ordering by title returns books in the expected order.

        Uses /books/?ordering=title to sort ascending by title.
        """
        response = self.client.get(self.list_url, {"ordering": "title"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = [b["title"] for b in response.data]
        self.assertEqual(
            titles,
            sorted(
                [self.book1.title, self.book2.title, self.book3.title]
            ),
        )

    def test_order_books_by_publication_year_desc(self):
        """
        Verify that ordering by -publication_year sorts books newest first.

        Uses /books/?ordering=-publication_year to sort descending by year.
        """
        response = self.client.get(self.list_url, {"ordering": "-publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [b["publication_year"] for b in response.data]
        self.assertEqual(years, sorted(years, reverse=True))
