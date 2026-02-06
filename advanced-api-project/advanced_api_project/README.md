# Advanced API Project - Custom & Generic Views

This project demonstrates how to use Django REST Framework’s generic views and customizations for CRUD operations on a `Book` model.

## Views Implemented
- **BookListView**: Retrieve all books (`/books/`)
- **BookDetailView**: Retrieve a single book by ID (`/books/<id>/`)
- **BookCreateView**: Add a new book (`/books/create/`) – requires authentication
- **BookUpdateView**: Modify an existing book (`/books/<id>/update/`) – requires authentication
- **BookDeleteView**: Remove a book (`/books/<id>/delete/`) – requires authentication

## Permissions
- List & Detail views: open to all users
- Create, Update, Delete views: restricted to authenticated users

## Testing
Use Postman or curl to test endpoints:
- `GET /books/`
- `GET /books/1/`
- `POST /books/create/`
- `PUT /books/1/update/`
- `DELETE /books/1/delete/`

Ensure permissions are enforced by testing with and without authentication.
