"""
This module is responsible for handling the Location entity.
"""

from .base import BaseRepository


class PostalCodeRepository(BaseRepository):
    """
    This class is responsible for handling the Postal Code entity.
    """
    def __init__(self):
        super().__init__("postal_codes")
