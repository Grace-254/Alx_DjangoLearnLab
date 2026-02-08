from bookshelf.models import Book

Book.objects.all()
# <QuerySet [<Book: 1984 by George Orwell>]>

book = Book.objects.first()
book.title
# '1984'
book.author
# 'George Orwell'
book.publication_year
# 1949
