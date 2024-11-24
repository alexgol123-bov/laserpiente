"""Game Renderer

This file can be imported as a module and contains the following classes:
    * Renderer
"""

from dataclasses import astuple

import pygame

from color import Color

from core.vector import Vector
from core.game_model import GameModel


class Renderer:
    """Class representing a game renderer.

    Attributes:
        _model (GameModel): a data model of the game
        _fps (int): FPS
        _scale (Vector): view scale
        _board_frame_size (Vector): a board frame size
        _window_size (Vector): a window size
        _window (pygame.Surface): a game window
        _board_frame (pygame.Surface): a game frame
        _fps_controller (pygame.Clock): a FPS controller
    """

    def __init__(self, title: str, model: GameModel) -> None:
        """Initialises a Renderer class object.

        Args:
            title (str): a game title
            model (GameModel): a data model of the game
        """

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
        """Initialises a game window.

        Args:
            title (str): a game title
        """
        pygame.init()
        pygame.display.set_caption(title)

        self._window = pygame.display.set_mode(astuple(self._window_size))
        self._board_frame = pygame.Surface(astuple(self._board_frame_size))

        self._fps_controller = pygame.time.Clock()

    def __del__(self) -> None:
        """Destructs a class object."""
        pygame.quit()

    def render(self) -> None:
        """Renders the game."""
        self._clear_window()

        self._draw_board()
        self._draw_info()

        pygame.display.update()
        self._update_fps()

    def _clear_window(self) -> None:
        """Clears a game window."""
        self._window.fill(Color.BLACK.value)
        self._board_frame.fill(Color.BLACK.value)

    def _draw_board(self) -> None:
        """Draws a game board."""
        self._draw_grid()
        self._draw_apple()
        self._draw_snake()

        self._window.blit(self._board_frame, (0, 0))

    def _draw_grid(self) -> None:
        """Draws a game board grid."""
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
        """Draws game information."""
        self._draw_score()
        self._draw_result()

    def _draw_score(self) -> None:
        """Draws the scores."""
        margin = 16
        font = pygame.font.SysFont("times", 16)
        surface = font.render(f"Score: {self._model.score}", True, Color.WHITE.value)
        self._window.blit(surface, (self._board_frame_size.x + margin, margin))

    def _draw_result(self) -> None:
        """Draws the result of the game."""
        if self._model.running:
            return

        margin = 16
        font = pygame.font.SysFont("times", 16)
        surface = font.render(f"You lost :(", True, Color.WHITE.value)
        self._window.blit(surface, (self._board_frame_size.x + margin, 4 * margin))

    def _draw_apple(self) -> None:
        """Draws an apple."""
        self._draw_object(self._model.apple.location, Color.RED)

    def _draw_object(self, location: Vector, color: Color) -> None:
        """Draws an object.

        Args:
            location (Vector): object location
            color (Color): object color
        """
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
        """Draws a snake."""
        for location in self._model.snake.body:
            self._draw_object(location, Color.GREEN)

    def _update_fps(self) -> None:
        """Updates FPS."""
        self._fps_controller.tick(self._fps)
