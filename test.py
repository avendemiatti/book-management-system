from database.db_connection import get_connection

def test_connection():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT version();")
            db_version = cur.fetchone()
            print("DB Version:", db_version)

test_connection()
