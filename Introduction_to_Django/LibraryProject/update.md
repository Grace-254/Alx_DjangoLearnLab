
#### 3. `update.md`

**File:** `Introduction_to_Django/bookshelf/update.md`

```markdown
# Update Operation

Command to update the title from "1984" to "Nineteen Eighty-Four".

```python
from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"

# Save the changes
book.save()

# Verify update
print(book.title)

# Expected Output: Nineteen Eighty-Four