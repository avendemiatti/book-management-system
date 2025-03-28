from database.db_connection import get_connection
from model.category import Category

class CategoryDAO:
    def __init__(self):
        """
        Constructor. For now, this was storing an in-memory list (self.categories),
        but since we will use PostgreSQL, we don't strictly need this list anymore.
        You can remove it if you want.
        """
        self.categories = []

    def list_all(self):
        """
        Retrieve all categories from the 'categorias' table via SQL.
        """
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id, nome FROM categorias")
                rows = cur.fetchall()
                
                categories = []
                for row in rows:
                    cat_id = row[0]
                    name = row[1]
                    category_obj = Category(cat_id, name)
                    categories.append(category_obj)
                
                return categories

    def create(self, category):

        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO categorias (nome) VALUES (%s) RETURNING id", (category.name,))
                category_id = cur.fetchone()[0]
                category.category_id = category_id
                conn.commit()


        self.categories.append(category)

    def delete(self, category_id):

        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM categorias WHERE id = %s", (category_id,))
                conn.commit()
        # Remove from in-memory list as well
        # This is optional, depending on whether you want to keep the in-memory list in sync
        # with the database.
        # If you want to keep it in sync, uncomment the next line

        self.categories = [cat for cat in self.categories if cat.category_id != category_id]

    def find_by_id(self, category_id):

        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id, nome FROM categorias WHERE id = %s", (category_id,))
                row = cur.fetchone()
                if row:
                    cat_id = row[0]
                    name = row[1]
                    return Category(cat_id, name)
                else:
                    return None
 