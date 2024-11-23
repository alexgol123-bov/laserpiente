import time

import pygame

from core.direction import Direction
from renderer import Renderer
from core.game_model import GameModel


class Game:
    """"""

    def __init__(self, title) -> None:
        self._model = GameModel()
        self._renderer = Renderer(title, self._model)

    def run(self) -> None:
        while self._model.running:
            self._process_input()
            self._update()
            self._render()

        time.sleep(3)

    def _process_input(self) -> None:
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
        self._model.update()

    def _render(self) -> None:
        self._renderer.render()
