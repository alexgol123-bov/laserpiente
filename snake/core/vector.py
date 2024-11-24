"""Coordinate vector

This file can be imported as a module and contains the following classes:
    * Vector
"""

from dataclasses import dataclass
from typing import Self


@dataclass
class Vector:
    """Class representing a coordinate vector (2D).

    Attributes:
        x (int): a value on the horizontal X-axis
        y (int): a value on the vertical Y-axis
    """

    x: int = 0
    y: int = 0

    def __add__(self, other: Self) -> Self:
        """Sums two vectors.

        Args:
            other (Vector): Another vector

        Returns:
            The sum of two vectors
        """
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __sub__(self, other: Self) -> Self:
        """Substructs two vectors.

        Args:
            other (Vector): Another vector

        Returns:
            The difference of two vectors
        """
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)

    def __mul__(self, value: int) -> Self:
        """Multiplies the vector by a scalar

        Args:
            value (int): a scalar

        Returns:
            The result of scalar multiplication
        """
        x = self.x * value
        y = self.y * value
        return Vector(x, y)

    def __truediv__(self, value: int) -> Self:
        """Divides the vector by a scalar.

        Args:
            value (int): a scalar

        Returns:
            The result of dividing the vector by a scalar
        """
        x = self.x / value
        y = self.y / value
        return Vector(x, y)

    def __eq__(self, other: Self) -> bool:
        """Check if two vectors are equal

        Args:
            other (Vector): Another vector

        Returns:
            true/false
        """
        return self.x == other.x and self.y == other.y

    def __ne__(self, other: Self) -> bool:
        """Check if two vectors are not equal

        Args:
            other (Vector): Another vector

        Returns:
            true/false
        """
        return not self == other
