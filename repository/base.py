"""
This module is responsible for handling the base repository.
"""

from typing import Any, Dict

from data.db import get_db_connection


class BaseRepository:
    """
    This class is responsible for handling the base repository.
    """
    table_name: str
    conn: Any
    cursor: Any

    def __init__(self, table_name: str):
        self.table_name = table_name
        self.conn = get_db_connection()

        self.cursor = self.conn.cursor()

    def create(self, data: Dict[str, Any]):
        """
        This method is responsible for creating a new record in the database.
        """
        keys = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        query = f"INSERT INTO {self.table_name} ({keys}) VALUES ({values})"
        self.cursor.execute(query, tuple(data.values()))
        self.conn.commit()

    def find_all(self):
        """
        This method is responsible for fetching all records from the database.
        """
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        return self.cursor.fetchall()

    def find_by_id(self, target_id: int):
        """
        This method is responsible for fetching a record by its ID from the database.
        """
        self.cursor.execute(f"SELECT * FROM {self.table_name} WHERE id = %s", (target_id,))
        return self.cursor.fetchone()

    def update(self, target_id: int, data: Dict[str, Any]):
        """
        This method is responsible for updating a record in the database.
        """
        keys_and_values = ', '.join([f"{key} = %s" for key in data.keys()])
        query = f"UPDATE {self.table_name} SET {keys_and_values} WHERE id = %s"
        self.cursor.execute(query, tuple(data.values()) + (target_id,))
        self.conn.commit()

    def delete(self, target_id: int):
        """
        This method is responsible for deleting a record from the database.
        """
        self.cursor.execute(f"DELETE FROM {self.table_name} WHERE id = %s", (target_id,))
        self.conn.commit()

# Path: repository/location.py
