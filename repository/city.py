"""
This module is responsible for handling the City entity.
"""

from .base import BaseRepository


class CityRepository(BaseRepository):
    """
    This class is responsible for handling the City entity.
    """
    def __init__(self):
        super().__init__("cities")
