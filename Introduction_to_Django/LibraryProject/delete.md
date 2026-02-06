
#### 4. `delete.md`

**File:** `Introduction_to_Django/bookshelf/delete.md`

```markdown
# Delete Operation

Command to delete the book and confirm deletion.

```python
from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Confirm deletion by checking all books
print(Book.objects.all())

# Expected Output: <QuerySet []>