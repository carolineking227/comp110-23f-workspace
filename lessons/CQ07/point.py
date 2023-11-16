"""Ex08 - more practice with OOP!"""
from __future__ import annotations


class Point:
    """Class to represent (x,y) coordinate point."""

    x: float
    y: float
    
    def __init__(self, init_x: float = 0.0, init_y: float = 0.0):
        """Construct a point with default values of 0.0 for x and y."""
        self.x = init_x
        self.y = init_y

    def scale_by(self, factor: int) -> None:
        """Modify (or mutate) a point."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Make a new point."""
        return Point(self.x * factor, self.y * factor)

    def __str__(self) -> str:
        """Return a string of the Point."""
        return f"x: {self.x}; y: {self.y}"

    def __mul__(self, factor: int) -> Point:
        """Multiply a Point by a factor (int or float)."""
        return Point(self.x * factor, self.y * factor)

    def __add__(self, factor: float) -> Point:
        """Add a factor (int or float) to the Point."""
        return Point(self.x + factor, self.y + factor)