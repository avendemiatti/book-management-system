# service/book_service.py

from dao.book_dao import BookDAO
from model.book import Book

class BookService:
    """
    Handles the business logic for Book-related operations.
    Calls the BookDAO for data persistence and retrieval.
    """

    def __init__(self):
        self.book_dao = BookDAO()

    def list_books(self):
        """
        Get a list of all Book objects.
        """
        return self.book_dao.list_all()

    def add_book(self, title, summary, year, pages, isbn, category_id, editor_id, author_id):
        new_book = Book(None, title, summary, year, pages, isbn, category_id, editor_id, author_id)
        self.book_dao.create(new_book)


    def delete_book(self, book_id):
        """
        Delete a Book by its ID.
        :param book_id: The ID of the book to remove.
        """
        self.book_dao.delete(book_id)

    def get_book_by_id(self, book_id):
        """
        Fetch a Book by ID.
        :param book_id: The ID of the book to retrieve.
        :return: The matching Book object or None if not found.
        """
        return self.book_dao.find_by_id(book_id)
