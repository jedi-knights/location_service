"""
This module contains the functionality to drop the database.
"""

import os

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from data.db import get_db_connection

if __name__ == "__main__":
    # Connect to the PostgreSQL server
    conn = get_db_connection()

    # Allow database operations
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Drop the database if it already exists
    cur.execute(f"DROP DATABASE IF EXISTS {os.getenv('DB_NAME')}")

    # Close the cursor and the connection
    cur.close()
    conn.close()
