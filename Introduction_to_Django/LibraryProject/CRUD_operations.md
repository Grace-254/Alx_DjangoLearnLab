
### Step 5: Create `CRUD_operations.md`

The task also asks for a master file named `CRUD_operations.md` in the root directory. Create this file at `Introduction_to_Django/CRUD_operations.md`.

**File:** `Introduction_to_Django/CRUD_operations.md`

```markdown
# CRUD Operations Documentation

This file documents the interactions performed with the Book model via the Django shell.

## 1. Create
Created a book titled "1984" by George Orwell.
Command: `Book.objects.create(title="1984", author="George Orwell", publication_year=1949)`

## 2. Retrieve
Retrieved the book using its title.
Command: `Book.objects.get(title="1984")`

## 3. Update
Updated the title to "Nineteen Eighty-Four".
Command: 
```python
book.title = "Nineteen Eighty-Four"
book.save()