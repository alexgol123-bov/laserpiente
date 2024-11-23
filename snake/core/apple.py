from dataclasses import dataclass

from core.vector import Vector


@dataclass
class Apple:
    location: Vector

    def rotate(self, rotator) -> None:
        self.location = rotator(self.location)
