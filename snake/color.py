"""Color

This file can be imported as a module and contains the following enums:
    * Color
"""

from enum import Enum


class Color(Enum):
    """Enum representing colour in RGB.

    Possible values:
        WHITE
        GREY
        BLACK
        RED
    """

    WHITE = (200, 200, 200)
    GREY = (10, 10, 10)
    BLACK = (5, 5, 5)
    GREEN = (0, 230, 0)
    RED = (230, 0, 0)
