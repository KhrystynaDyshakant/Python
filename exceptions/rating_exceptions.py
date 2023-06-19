"""
This module defines custom expection classes related to ratings.
"""

class RatingException(Exception):
    """
    Exception occurs when invalid rating is invalid.
    Args:
        message(str): The error message that describes invalid rating
    """
    message = "Rating should be from 1 to 5"

    def __init__(self):
        super().__init__(self.message)
