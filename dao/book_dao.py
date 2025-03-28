# dao/book_dao.py

from model.book import Book

class BookDAO:
    """
    DAO for Book entities.
    Stores Book data in a list for now, to be replaced with real DB calls later.
    """

    def __init__(self):
        """
        Initialize an empty list to hold Book instances.
        """
        self.books = []

    def create(self, book):
        """
        Add a new Book to the list.
        :param book: An instance of the Book class.
        """
        self.books.append(book)

    def list_all(self):
        """
        Return all Book objects in our in-memory store.
        :return: List of Book instances.
        """
        return self.books

    def find_by_id(self, book_id):
        """
        Find a Book by its ID.
        :param book_id: The ID of the Book to locate.
        :return: The Book object if found, else None.
        """
        for bk in self.books:
            if bk.book_id == book_id:
                return bk
        return None

    def delete(self, book_id):
        """
        Delete a Book by its ID.
        :param book_id: The ID of the Book to delete.
        """
        self.books = [bk for bk in self.books if bk.book_id != book_id]
