# dao/author_dao.py

from database.db_connection import get_connection
from model.author import Author

class AuthorDAO:
    def __init__(self):
        # No in-memory list needed if we're using PostgreSQL
        pass

    def create(self, author):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO book.autores (nome, email, telefone, bio) VALUES (%s, %s, %s, %s) RETURNING id",
                    (author.name, author.email, author.phone, author.bio)
                )
                author_id = cur.fetchone()[0]
                author.author_id = author_id
                conn.commit()

        # Remove self.authors.append(author) because we rely on the DB, not an in-memory list

    def list_all(self):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id, nome, email, telefone, bio FROM book.autores")
                rows = cur.fetchall()

                authors = []
                for row in rows:
                    author_id = row[0]
                    name = row[1]
                    email = row[2]
                    phone = row[3]
                    bio = row[4]
                    author_obj = Author(author_id, name, email, phone, bio)
                    authors.append(author_obj)

                return authors

    def find_by_id(self, author_id):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT id, nome, email, telefone, bio FROM book.autores WHERE id = %s",
                    (author_id,)
                )
                row = cur.fetchone()
                if row:
                    author_id = row[0]
                    name = row[1]
                    email = row[2]
                    phone = row[3]
                    bio = row[4]
                    return Author(author_id, name, email, phone, bio)
                return None

    def delete(self, author_id):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "DELETE FROM book.autores WHERE id = %s",
                    (author_id,)
                )
                conn.commit()
