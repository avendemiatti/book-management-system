# dao/category_dao.py

from database.db_connection import get_connection
from model.category import Category

class CategoryDAO:
    def __init__(self):
        """
        Constructor. We no longer keep an in-memory list, since
        all data is stored in the PostgreSQL database under the 'book' schema.
        """
        pass

    def list_all(self):
        """
        Retrieve all categories from the 'book.categorias' table via SQL.
        """
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id, nome FROM book.categorias")
                rows = cur.fetchall()
                
                categories = []
                for row in rows:
                    cat_id = row[0]
                    name = row[1]
                    category_obj = Category(cat_id, name)
                    categories.append(category_obj)
                
                return categories

    def create(self, category):
        """
        Insert a new category record into 'book.categorias',
        returning and setting the auto-generated ID in the category object.
        """
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO book.categorias (nome) VALUES (%s) RETURNING id",
                    (category.name,)
                )
                category_id = cur.fetchone()[0]
                category.category_id = category_id
                conn.commit()

    def delete(self, category_id):
        """
        Delete a category from 'book.categorias' by its ID.
        """
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "DELETE FROM book.categorias WHERE id = %s",
                    (category_id,)
                )
                conn.commit()

    def find_by_id(self, category_id):
        """
        Find a category by ID in 'book.categorias'.
        :return: A Category object if found, otherwise None.
        """
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT id, nome FROM book.categorias WHERE id = %s",
                    (category_id,)
                )
                row = cur.fetchone()
                if row:
                    cat_id, name = row
                    return Category(cat_id, name)
                else:
                    return None

    def update(self, category):
        """
        Update the 'nome' of an existing record in 'book.categorias'.
        """
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE book.categorias SET nome = %s WHERE id = %s",
                    (category.name, category.category_id)
                )
                conn.commit()
