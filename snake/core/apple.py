"""Apple

This file can be imported as a module and contains the following classes:
    * Apple
"""

from core.vector import Vector


class Apple:
    """Class representing an apple.

    Attributes:
        location (Vector): apple location
    """

    def __init__(self, location: Vector) -> None:
        """Initialises an Apple class object.

        Args:
            location (Vector): apple location
        """

        self.location = location

    def rotate(self, rotator) -> None:
        """Rotates the apple.

        Args:
            rotator (obj): function which rotates the apple
        """
        self.location = rotator(self.location)
