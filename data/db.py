"""
This module contains the function to connect to the database.
"""

import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


def get_db_connection():
    """
    Connect to the PostgreSQL database
    """
    # Connect to the PostgreSQL server
    conn = psycopg2.connect(
        dbname="postgres",
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

    return conn
