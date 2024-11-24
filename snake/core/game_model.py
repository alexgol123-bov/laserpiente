"""Game Model

This file can be imported as a module and contains the following classes:
    * GameModel
"""

import random

from core.apple import Apple
from core.direction import Direction
from core.snake import Snake
from core.vector import Vector


class GameModel:
    """Class representing a data model of the game.

    Attributes:
        _board_size (Vector): a virtual board size
        running (bool): a flag that indicates if the game is still in progress
        _score (int): a game score
        _snake (Snake): a snake
        _apple (Apple): an apple
    """

    def __init__(self) -> None:
        """Initialises a GameModel class object."""
        self._board_size = Vector(40, 40)
        self.running = True
        self._score = 0

        self.__init_snake()
        self._generate_apple()

    def __init_snake(self) -> None:
        """Initialises _snake."""
        location = self._board_size / 2
        self._snake = Snake(location)

    def _generate_apple(self) -> None:
        """Initialises _apple."""
        self._apple = Apple(self._random_location())

    def _random_location(self) -> Vector:
        """Gets random location.

        Returns:
            A random vector
        """
        x = random.randint(0, self._board_size.x)
        y = random.randint(0, self._board_size.y)
        return Vector(x, y)

    @property
    def score(self) -> int:
        """Gets the score.

        Returns:
            The score
        """
        return self._score

    @property
    def board_size(self) -> Vector:
        """Gets the board size.

        Returns:
            The board size
        """
        return self._board_size

    @property
    def snake(self) -> Snake:
        """Gets the snake.

        Returns:
            The snake
        """
        return self._snake

    @property
    def apple(self) -> Apple:
        """Gets the apple.

        Returns:
            The apple
        """
        return self._apple

    def rotate(self, direction: Direction) -> None:
        """Rotates the board and all its objects.

        Args:
            direction (Direction): turning direction
        """
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
        """Gets the snake"""
        if self._is_apple_eaten():
            self._score += 1
            self._snake.grow()
            self._generate_apple()

        self._snake.move()

        if self._has_collitions():
            self.running = False

    def _is_apple_eaten(self) -> bool:
        """Check if the apple is eaten.

        Returns:
            True/False
        """
        return self._apple.location == self._snake.head

    def _has_collitions(self) -> bool:
        """Check if there any collitions.

        Returns:
            True/False
        """
        return self._is_snake_out_of_board() or self._snake_ran_into_itself()

    def _is_snake_out_of_board(self) -> bool:
        """Check if the snake is out of the board.

        Returns:
            True/False
        """
        return (
            self._snake.head.x < 0
            or self._snake.head.x > self._board_size.x
            or self._snake.head.y < 0
            or self._snake.head.y > self._board_size.y
        )

    def _snake_ran_into_itself(self) -> bool:
        """Check if the snake ran into itself.

        Returns:
            True/False
        """
        return self._snake.head in self._snake.body[1:]
