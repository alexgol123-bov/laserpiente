import sys
import random

import pygame

from core.types.vector import Vector
from core.snake import Snake
from core.apple import Apple
from core.direction import Direction
from color import Color


class Game:
    """"""

    def __init__(self, title) -> None:
        self._board_size = Vector(40, 40)
        self._scale = Vector(10, 10)
        self._fps = 16

        self._score = 0

        self._running = True

        self.__init_window(title)
        self.__init_snake()
        self._generate_apple()

    def __init_window(self, title) -> None:
        pygame.init()
        pygame.display.set_caption(title)

        window_size = (
            (self._board_size.x + 1) * self._scale.x,
            (self._board_size.y + 1) * self._scale.y,
        )
        self._window = pygame.display.set_mode(window_size)
        self._fps_controller = pygame.time.Clock()

    def __init_snake(self) -> None:
        location = self._board_size / 2
        self._snake = Snake(location)

    def _generate_apple(self) -> None:
        self._apple = Apple(self._random_location())

    def _random_location(self) -> Vector:
        x = random.randint(0, self._board_size.x)
        y = random.randint(0, self._board_size.y)
        return Vector(x, y)

    def __del__(self) -> None:
        pygame.quit()

    def run(self) -> None:
        self._render_rules()

        while self._running:
            self._process_input()
            self._update()
            self._render_game()

    def _render_rules(self) -> None:
        # todo
        ...

    def _process_input(self) -> None:
        eventypes = (pygame.KEYDOWN, pygame.QUIT)
        direction = None

        for event in pygame.event.get(eventtype=eventypes):
            match event.type:
                case pygame.QUIT:
                    self._running = False
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_LEFT:
                            direction = Direction.LEFT
                        case pygame.K_RIGHT:
                            direction = Direction.RIGHT
                        case pygame.K_ESCAPE:
                            self._running = False

        if self._running == False or direction is None:
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

    def _update(self) -> None:
        if self._is_apple_eaten():
            self._score += 1
            self._snake.grow()
            self._generate_apple()

        self._snake.move()

        if self._has_collapses():
            self._running = False

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

    def _render_game(self) -> None:
        self._clear_window()

        self._render_apple()
        self._render_snake()

        pygame.display.update()
        self._update_fps()

    def _clear_window(self) -> None:
        self._window.fill(Color.BLACK.value)

    def _render_apple(self) -> None:
        self._render_object(self._apple.location, Color.RED)

    def _render_object(self, location: Vector, color: Color) -> None:
        pygame.draw.rect(
            self._window,
            color.value,
            pygame.Rect(
                location.x * self._scale.x,
                location.y * self._scale.y,
                self._scale.x,
                self._scale.y,
            ),
        )

    def _render_snake(self) -> None:
        for location in self._snake.body:
            self._render_object(location, Color.GREEN)

    def _update_fps(self) -> None:
        self._fps_controller.tick(self._fps)
