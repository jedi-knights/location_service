"""
This module is responsible for handling the Country entity.
"""

from .base import BaseRepository


class CountryRepository(BaseRepository):
    """
    This class is responsible for handling the Country entity.
    """
    def __init__(self):
        super().__init__("countries")
