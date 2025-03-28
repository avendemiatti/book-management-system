# service/author_service.py

from dao.author_dao import AuthorDAO
from model.author import Author

class AuthorService:
    """
    The AuthorService class handles all "business logic" related to authors.
    It delegates direct data operations to the AuthorDAO.
    """

    def __init__(self):
        # Instantiate the DAO (using in-memory storage for now)
        self.author_dao = AuthorDAO()

    def list_authors(self):
        """
        Retrieve all authors via the DAO.
        :return: List of all Author objects.
        """
        return self.author_dao.list_all()

    def add_author(self, author_id, name, email, phone, bio):
        """
        Create a new Author object and pass it to the DAO.
        This is where you could add validation or checks before saving.
        :param author_id: Unique author identifier.
        :param name: Author's name.
        :param email: Author's email address.
        :param phone: Author's phone number.
        :param bio: Author's short biography.
        """
        # In a real system, you might validate (e.g., check if email is valid).
        new_author = Author(author_id, name, email, phone, bio)
        self.author_dao.create(new_author)

    def delete_author(self, author_id):
        """
        Remove the author with the specified ID.
        :param author_id: Unique identifier of the author to delete.
        """
        self.author_dao.delete(author_id)

    def get_author_by_id(self, author_id):
        """
        Get a single author by ID.
        :param author_id: The author ID to look up.
        :return: The Author object if found, otherwise None.
        """
        return self.author_dao.find_by_id(author_id)
