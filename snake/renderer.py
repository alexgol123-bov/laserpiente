import pygame

from color import Color

from core.types.vector import Vector
from game_model import GameModel


class Renderer:
    def __init__(self, title: str, model: GameModel) -> None:
        self._model = model

        self._fps = 16
        self._scale = Vector(10, 10)
        self._frame_size = (
            (self._model.board_size.x + 1) * self._scale.x,
            (self._model.board_size.y + 1) * self._scale.y,
        )

        self.__init_window(title)

    def __init_window(self, title) -> None:
        pygame.init()
        pygame.display.set_caption(title)

        self._window = pygame.display.set_mode(self._frame_size)
        self._fps_controller = pygame.time.Clock()

    def __del__(self) -> None:
        pygame.quit()

    def render(self) -> None:
        self._clear_window()

        self._render_apple()
        self._render_snake()

        pygame.display.update()
        self._update_fps()

    def _clear_window(self) -> None:
        self._window.fill(Color.BLACK.value)

    def _render_apple(self) -> None:
        self._render_object(self._model.apple.location, Color.RED)

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
        for location in self._model.snake.body:
            self._render_object(location, Color.GREEN)

    def _update_fps(self) -> None:
        self._fps_controller.tick(self._fps)
