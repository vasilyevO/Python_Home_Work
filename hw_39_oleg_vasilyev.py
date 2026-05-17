print("\n 1. Фигуры и площади")

from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    """An abstract shape class."""

    @abstractmethod
    def area(self) -> float:
        """Returns the area of the shape."""

class Circle(Shape):
    """"Circle class."""

    def __init__(self, radius: float) -> None:
        """
        Args:
            radius: radius of a circle.
        """
        self.radius = radius

    def area(self) -> float:
        """Returns the area of a circle: π * r²."""
        return pi * self.radius ** 2

class Rectangle(Shape):
    """The Rectangle class."""

    def __init__(self, width: float, height: float) -> None:
        """
        Args:
            width: the width of the rectangle.
            height: the height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self) -> float:
        """Returns the area of a rectangle: width * height."""
        return self.width * self.height

shapes = [Circle(3), Rectangle(4, 5)]
for shape in shapes:
    print(f"Area: {shape.area():.2f}")


print("\n 2. Проверка размеров фигур")

from abc import ABC, abstractmethod
from math import pi

class InvalidSizeError(Exception):
    """Exception for incorrect shape dimensions."""
    pass

class Shape(ABC):
    """An abstract shape class."""

    @abstractmethod
    def area(self) -> float:
        """Returns the area of the shape."""


class Circle(Shape):
    """Circle class."""

    def __init__(self, radius: float) -> None:
        """
        Args:
            radius: radius of a circle.

        Raises:
            InvalidSizeError: if the radius is not positive.
        """
        if radius <= 0:
            raise InvalidSizeError("Размер должен быть положительным!")
        self.radius = radius

    def area(self) -> float:
        """Returns the area of a circle: π * r²."""
        return pi * self.radius ** 2


class Rectangle(Shape):
    """The Rectangle class."""

    def __init__(self, width: float, height: float) -> None:
        """
        Args:
            width: the width of the rectangle.
            height: the height of the rectangle.

        Raises:
            InvalidSizeError: if the width or height is not positive.
        """
        if width <= 0 or height <= 0:
            raise InvalidSizeError("Размер должен быть положительным!")
        self.width = width
        self.height = height

    def area(self) -> float:
        """Returns the area of a rectangle: width * height."""
        return self.width * self.height

shapes = [Circle(3), Rectangle(4, 5)]
for shape in shapes:
    print(f"Area: {shape.area():.2f}")

try:
    c = Circle(-5)
except InvalidSizeError as e:
    print(f"InvalidSizeError: {e}")

try:
    r = Rectangle(0, 5)
except InvalidSizeError as e:
    print(f"InvalidSizeError: {e}")