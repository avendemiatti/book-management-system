# dao/author_dao.py

from model.author import Author

class AuthorDAO:

    def __init__(self):

        self.authors = []

    def create(self, author):

        self.authors.append(author)

    def list_all(self):

        return self.authors

    def find_by_id(self, author_id):
 
        for author in self.authors:
            if author.author_id == author_id:
                return author
        return None

    def delete(self, author_id):

        self.authors = [author for author in self.authors if author.author_id != author_id]
