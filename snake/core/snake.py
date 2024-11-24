"""Snake

This file can be imported as a module and contains the following classes:
    * Snake
"""

from core.vector import Vector
from core.direction import Direction


class Snake:
    """Class representing a snake.

    Attributes:
        __head_index (int): the index of the snake head

        _direction (Direction): snake direction
        _body (list[Vector]): snake body
    """

    __head_index: int = 0

    def __init__(self, location: Vector) -> None:
        """Initialises a Snake class object.

        Args:
            location (Vector): snake location
        """
        self._direction = Direction.UP
        self._body = [location - self._direction.value * i for i in range(3)]

    @property
    def head(self) -> Vector:
        """Gets snake head location.

        Returns:
            Snake head location
        """
        return self._body[self.__head_index]

    @property
    def body(self) -> list[Vector]:
        """Gets snake body location.

        Returns:
            Snake body location
        """
        return self._body

    @property
    def direction(self) -> Direction:
        """Gets snake direction.

        Returns:
            Snake direction
        """
        return self._direction

    def rotate(self, rotator) -> None:
        """Rotates the snake.

        Args:
            rotator (obj): a function which rotates the snake
        """
        self._body[:] = map(rotator, self._body)

    def grow(self) -> None:
        """Grows the snake tail."""
        head_location = self.head + self._direction.value
        self._body.insert(self.__head_index, head_location)

    def move(self) -> None:
        """Moves the snake."""
        self.grow()
        self._body.pop()
