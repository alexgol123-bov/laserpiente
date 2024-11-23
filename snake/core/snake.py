from core.vector import Vector
from core.direction import Direction


class Snake:
    """"""

    __head_index = 0

    def __init__(self, location: Vector) -> None:
        self._direction = Direction.UP
        self._body = [location - self._direction.value * i for i in range(3)]

    @property
    def head(self) -> Vector:
        return self._body[self.__head_index]

    @property
    def body(self) -> list[Vector]:
        return self._body

    @property
    def direction(self) -> Direction:
        return self._direction

    def rotate(self, rotator) -> None:
        self._body[:] = map(rotator, self._body)

    def grow(self) -> None:
        head_location = self.head + self._direction.value
        self._body.insert(self.__head_index, head_location)

    def move(self) -> None:
        self.grow()
        self._body.pop()
