from core.types.vector import Vector
from core.direction import Direction


class Snake:
    """"""

    __head_index = 0

    def __init__(self, location: Vector, direction: Direction) -> None:
        self._direction = direction
        self._body = [
            location,
            location - self._direction.value,
            location - self._direction.value * 2,
        ]

    @property
    def head(self) -> Vector:
        return self._body[self.__head_index]

    @property
    def body(self) -> list[Vector]:
        return self._body

    @property
    def direction(self) -> Direction:
        return self._direction

    def turn(self, direction: Direction) -> None:
        if direction is None:
            return

        match (self._direction, direction):
            case (
                (Direction.UP, Direction.DOWN)
                | (Direction.DOWN, Direction.UP)
                | (Direction.RIGHT, Direction.LEFT)
                | (Direction.LEFT, Direction.RIGHT)
            ):
                return

        self._direction = direction

    def grow(self) -> None:
        head_location = self.head + self._direction.value
        self._body.insert(self.__head_index, head_location)

    def move(self) -> None:
        self.grow()
        self._body.pop()
