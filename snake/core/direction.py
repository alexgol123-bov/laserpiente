"""Direction

This file can be imported as a module and contains the following enums:
    * Direction
"""

from enum import Enum

from core.vector import Vector


class Direction(Enum):
    """Enum representing direction of movement.

    Possible values:
        UP (Vector)
        DOWN (Vector)
        LEFT (Vector)
        RIGHT (Vector)
    """

    UP = Vector(0, -1)
    DOWN = Vector(0, 1)
    LEFT = Vector(-1, 0)
    RIGHT = Vector(1, 0)
