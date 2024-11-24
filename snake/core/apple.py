from core.vector import Vector


class Apple:
    def __init__(self, location: Vector) -> None:
        self.location = location

    def rotate(self, rotator) -> None:
        self.location = rotator(self.location)
