from enum import Enum

from core.vector import Vector


class Direction(Enum):
    UP = Vector(0, -1)
    DOWN = Vector(0, 1)
    LEFT = Vector(-1, 0)
    RIGHT = Vector(1, 0)
