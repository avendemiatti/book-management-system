# dao/book_dao.py
from database.db_connection import get_connection
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
        pass

    def create(self, book):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO book.livros (titulo, resumo, ano, paginas, isbn, id_categoria, id_editora, id_autor) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id",
                    (book.title, book.summary, book.year, book.pages, book.isbn, book.category_id, book.editor_id, book.author_id)
                )
                book_id = cur.fetchone()[0]
                book.book_id = book_id
                conn.commit()
                return book

    def list_all(self):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id, titulo, resumo, ano, paginas, isbn, id_categoria, id_editora, id_autor FROM book.livros")
                rows = cur.fetchall()

                books = []
                for row in rows:
                    book_id = row[0]
                    title = row[1]
                    summary = row[2]
                    year = row[3]
                    pages = row[4]
                    isbn = row[5]
                    category_id = row[6]
                    editor_id = row[7]
                    author_id = row[8]
                    book_obj = Book(book_id, title, summary, year, pages, isbn, category_id, editor_id, author_id)
                    books.append(book_obj)
                return books

    def find_by_id(self, book_id):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT id, titulo, resumo, ano, paginas, isbn, id_categoria, id_editora, id_autor FROM book.livros WHERE id = %s",
                    (book_id,)
                )
                row = cur.fetchone()
                if row:
                    book_id = row[0]
                    title = row[1]
                    summary = row[2]
                    year = row[3]
                    pages = row[4]
                    isbn = row[5]
                    category_id = row[6]
                    editor_id = row[7]
                    author_id = row[8]
                    return Book(book_id, title, summary, year, pages, isbn, category_id, editor_id, author_id)
                return None

    def delete(self, book_id):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "DELETE FROM book.livros WHERE id = %s",
                    (book_id,)
                )
                conn.commit()
