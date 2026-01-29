from relationship_app.models import Author, Book, Library, Librarian

def run():
    # Query 1: All books by a specific author
    author = Author.objects.get(name="Jane Doe")
    books_by_author = Book.objects.filter(author=author)
    print("Books by Jane Doe:", [b.title for b in books_by_author])

    # Query 2: All books in a specific library
    library = Library.objects.get(name="City Library")
    books_in_library = library.books.all()
    print("Books in City Library:", [b.title for b in books_in_library])

    # Query 3: Retrieve the librarian for a library
    librarian = library.librarian
    print("Librarian for City Library:", librarian.name)
