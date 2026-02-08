
### CRUD_operations.md

```markdown
# CRUD operations for Book model

## Create

```python
from bookshelf.models import Book
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
# Book created successfully
