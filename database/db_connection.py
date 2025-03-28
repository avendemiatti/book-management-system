# database/db_connection.py

import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

def get_connection():
    """
    Returns a new psycopg2 connection using environment variables.
    Make sure you have PGHOST, PGDATABASE, PGUSER, and PGPASSWORD set in your .env file.
    """
    try:
        conn = psycopg2.connect(
            host=os.getenv("PGHOST"),
            database=os.getenv("PGDATABASE"),
            user=os.getenv("PGUSER"),
            password=os.getenv("PGPASSWORD"),
            port=os.getenv("PGPORT")  # if you have PGPORT in your .env
        )
        return conn
    except Exception as e:
        print("Erro ao estabelecer conexão com o banco de dados:", e)
        # Optionally re-raise or return None
        raise
