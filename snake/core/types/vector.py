from dataclasses import dataclass
from typing import Self


@dataclass
class Vector:
    """Class representing a coordinate vector."""

    x: int = 0
    y: int = 0

    def __add__(self, other: Self) -> Self:
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __sub__(self, other: Self) -> Self:
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)

    def __mul__(self, value: int) -> Self:
        x = self.x * value
        y = self.y * value
        return Vector(x, y)

    def __truediv__(self, value: int) -> Self:
        x = self.x / value
        y = self.y / value
        return Vector(x, y)

    def __eq__(self, other: Self) -> bool:
        return self.x == other.x and self.y == other.y

    def __ne__(self, other: Self) -> bool:
        return not self == other
