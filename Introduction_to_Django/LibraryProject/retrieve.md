
#### 2. `retrieve.md`

**File:** `Introduction_to_Django/bookshelf/retrieve.md`

```markdown
# Retrieve Operation

Command to retrieve and display the book just created.

```python
from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="1984")

# Display attributes
print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")

# Expected Output: Title: 1984, Author: George Orwell, Year: 1949