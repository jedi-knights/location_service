"""
This module is responsible for handling the Location entity.
"""

from .base import BaseRepository


class LocationRepository(BaseRepository):
    """
    This class is responsible for handling the Location entity.
    """
    def __init__(self):
        super().__init__("locations")
