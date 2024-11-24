"""Game

This file can be imported as a module and contains the following classes:
    * Game
"""

import time

import pygame

from core.direction import Direction
from renderer import Renderer
from core.game_model import GameModel


class Game:
    """Class representing the game.

    Attributes:
        _model (GameModel): a data model of the game
        _renderer (Renderer): a game renderer
    """

    def __init__(self, title: str) -> None:
        """Initialises a GameModel class object.

        Args:
            title (str): a game title
        """
        self._model = GameModel()
        self._renderer = Renderer(title, self._model)

    def run(self) -> None:
        """Runs the game."""
        while self._model.running:
            self._process_input()
            self._update()
            self._render()

        time.sleep(3)

    def _process_input(self) -> None:
        """Processes the input."""
        eventypes = (pygame.KEYDOWN, pygame.QUIT)
        direction = None

        for event in pygame.event.get(eventtype=eventypes):
            match event.type:
                case pygame.QUIT:
                    self._model.running = False
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_LEFT:
                            direction = Direction.LEFT
                        case pygame.K_RIGHT:
                            direction = Direction.RIGHT
                        case pygame.K_ESCAPE:
                            self._model.running = False

        if direction is not None:
            self._model.rotate(direction)

    def _update(self) -> None:
        """Updates the data model of the game."""
        self._model.update()

    def _render(self) -> None:
        """Renders the game."""
        self._renderer.render()
