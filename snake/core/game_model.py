import random

from core.apple import Apple
from core.direction import Direction
from core.snake import Snake
from core.types.vector import Vector


class GameModel:
    def __init__(self) -> None:
        self._board_size = Vector(40, 40)
        self.running = True
        self._score = 0

        self.__init_snake()
        self._generate_apple()

    def __init_snake(self) -> None:
        location = self._board_size / 2
        self._snake = Snake(location)

    def _generate_apple(self) -> None:
        self._apple = Apple(self._random_location())

    def _random_location(self) -> Vector:
        x = random.randint(0, self._board_size.x)
        y = random.randint(0, self._board_size.y)
        return Vector(x, y)

    @property
    def score(self) -> int:
        return self._score

    @property
    def board_size(self) -> Vector:
        return self._board_size

    @property
    def snake(self) -> Snake:
        return self._snake

    @property
    def apple(self) -> Apple:
        return self._apple

    def rotate(self, direction: Direction) -> None:
        if self.running == False or direction is None:
            return

        rotator = None
        match direction:
            case Direction.RIGHT:
                rotator = lambda location: Vector(
                    location.y,
                    min(self._board_size.x - location.x, self._board_size.x),
                )
            case Direction.LEFT:
                rotator = lambda location: Vector(
                    min(self._board_size.y - location.y, self._board_size.y),
                    location.x,
                )

        self._snake.rotate(rotator)
        self._apple.rotate(rotator)

    def update(self) -> None:
        if self._is_apple_eaten():
            self._score += 1
            self._snake.grow()
            self._generate_apple()

        self._snake.move()

        if self._has_collapses():
            self.running = False

    def _is_apple_eaten(self) -> bool:
        return self._apple.location == self._snake.head

    def _has_collapses(self) -> bool:
        return self._is_snake_out_of_board() or self._snake_ran_into_itself()

    def _is_snake_out_of_board(self) -> bool:
        return (
            self._snake.head.x < 0
            or self._snake.head.x > self._board_size.x
            or self._snake.head.y < 0
            or self._snake.head.y > self._board_size.y
        )

    def _snake_ran_into_itself(self) -> bool:
        return self._snake.head in self._snake.body[1:]
