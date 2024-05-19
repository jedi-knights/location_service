"""
This module is responsible for handling the State entity.
"""

from .base import BaseRepository


class StateRepository(BaseRepository):
    """
    This class is responsible for handling the State entity.
    """
    def __init__(self):
        super().__init__("states")
