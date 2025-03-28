from database.db_connection import get_connection
from model.editor import Editor

class EditorDAO:
    def __init__(self):
        """
        Constructor. We no longer keep an in-memory list, since
        all data is stored in the PostgreSQL database under the 'book' schema.
        """
        pass

    def create(self, editor):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO book.editoras (nome, endereco, telefone) VALUES (%s, %s, %s) RETURNING id",
                    (editor.name, editor.address, editor.phone)
                )
                editor_id = cur.fetchone()[0]
                editor.editor_id = editor_id
                conn.commit()

    def list_all(self):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id, nome, endereco, telefone FROM book.editoras")
                rows = cur.fetchall()

                editors = []
                for row in rows:
                    editor_id = row[0]
                    name = row[1]
                    address = row[2]
                    phone = row[3]
                    editor_obj = Editor(editor_id, name, address, phone)
                    editors.append(editor_obj)
                return editors

    def find_by_id(self, editor_id):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT id, nome, endereco, telefone FROM book.editoras WHERE id = %s",
                    (editor_id,)
                )
                row = cur.fetchone()
                if row:
                    editor_id = row[0]
                    name = row[1]
                    address = row[2]
                    phone = row[3]
                    return Editor(editor_id, name, address, phone)
                return None

    def delete(self, editor_id):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "DELETE FROM book.editoras WHERE id = %s",
                    (editor_id,)
                )
                conn.commit()