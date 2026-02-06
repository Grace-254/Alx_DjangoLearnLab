CREATE
python manage.py shell
from bookshelf.models import Book
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
book

RETRIEVE
python manage.py shell
from bookshelf.models import Book
books = Book.objects.all()
for b in books:
    print(b.id, b.title, b.author, b.publication_year)

UPDATE
python manage.py shell
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book

DELETE
python manage.py shell
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()
