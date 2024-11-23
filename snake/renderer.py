from dataclasses import astuple

import pygame

from color import Color

from core.types.vector import Vector
from core.game_model import GameModel


class Renderer:
    def __init__(self, title: str, model: GameModel) -> None:
        self._model = model

        self._fps = 16
        self._scale = Vector(10, 10)
        self._board_frame_size = Vector(
            (self._model.board_size.x + 1) * self._scale.x,
            (self._model.board_size.y + 1) * self._scale.y,
        )
        self._window_size = self._board_frame_size + Vector(200, 0)

        self.__init_window(title)

    def __init_window(self, title) -> None:
        pygame.init()
        pygame.display.set_caption(title)

        self._window = pygame.display.set_mode(astuple(self._window_size))
        self._board_frame = pygame.Surface(astuple(self._board_frame_size))

        self._fps_controller = pygame.time.Clock()

    def __del__(self) -> None:
        pygame.quit()

    def render(self) -> None:
        self._clear_window()

        self._draw_board()
        self._draw_info()

        pygame.display.update()
        self._update_fps()

    def _clear_window(self) -> None:
        self._window.fill(Color.BLACK.value)
        self._board_frame.fill(Color.BLACK.value)

    def _draw_board(self) -> None:
        self._draw_grid()
        self._draw_apple()
        self._draw_snake()

        self._window.blit(self._board_frame, (0, 0))

    def _draw_grid(self) -> None:
        for x in range(self._model.board_size.x + 1):
            scaled_x = x * self._scale.x
            pygame.draw.line(
                self._board_frame,
                Color.GREY.value,
                (scaled_x, 0),
                (scaled_x, self._board_frame_size.x),
            )

        for y in range(self._model.board_size.y + 1):
            scaled_y = y * self._scale.y
            pygame.draw.line(
                self._board_frame,
                Color.GREY.value,
                (0, scaled_y),
                (self._board_frame_size.x, scaled_y),
            )

    def _draw_info(self) -> None:
        self._draw_score()
        self._draw_result()

    def _draw_score(self) -> None:
        margin = 16
        font = pygame.font.SysFont("times", 16)
        surface = font.render(f"Score: {self._model.score}", True, Color.WHITE.value)
        self._window.blit(surface, (self._board_frame_size.x + margin, margin))

    def _draw_result(self) -> None:
        if self._model.running:
            return

        margin = 16
        font = pygame.font.SysFont("times", 16)
        surface = font.render(f"You lost :(", True, Color.WHITE.value)
        self._window.blit(surface, (self._board_frame_size.x + margin, 4 * margin))

    def _draw_apple(self) -> None:
        self._draw_object(self._model.apple.location, Color.RED)

    def _draw_object(self, location: Vector, color: Color) -> None:
        pygame.draw.rect(
            self._board_frame,
            color.value,
            pygame.Rect(
                location.x * self._scale.x,
                location.y * self._scale.y,
                self._scale.x,
                self._scale.y,
            ),
        )

    def _draw_snake(self) -> None:
        for location in self._model.snake.body:
            self._draw_object(location, Color.GREEN)

    def _update_fps(self) -> None:
        self._fps_controller.tick(self._fps)
