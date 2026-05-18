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
    """Circle class with validation via property."""

    def __init__(self, radius: float) -> None:
        self.radius = radius

    @property
    def radius(self) -> float:
        """Getter — возвращает радиус."""
        return self.__radius

    @radius.setter
    def radius(self, value: float) -> None:
        """Setter — validates and saves the radius."""
        if not isinstance(value, int | float):
            raise TypeError("Вы должны ввести цифры.")
        if value <= 0:
            raise InvalidSizeError("Размер должен быть положительным!")
        self.__radius = value

    def area(self) -> float:
        """Returns the area of a circle: π * r²."""
        return pi * self.radius ** 2

class Rectangle(Shape):
    """A rectangle class with validation via a property."""

    def __init__(self, width: float, height: float) -> None:
        self.width = width    # вызывает setter!
        self.height = height  # вызывает setter!

    @property
    def width(self) -> float:
        """Getter — returns the width."""
        return self.__width

    @width.setter
    def width(self, value: float) -> None:
        """Setter — validates and preserves the width."""
        if not isinstance(value, int | float):
            raise TypeError("Вы должны ввести цифры.")
        if value <= 0:
            raise InvalidSizeError("Размер должен быть положительным!")
        self.__width = value

    @property
    def height(self) -> float:
        """Getter — returns the height."""
        return self.__height

    @height.setter
    def height(self, value: float) -> None:
        """Setter — validates and saves the height."""
        if not isinstance(value, int | float):
            raise TypeError("Вы должны ввести цифры.")
        if value <= 0:
            raise InvalidSizeError("Размер должен быть положительным!")
        self.__height = value

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
    c = Circle("abc")
except TypeError as e:
    print(f"TypeError: {e}")

try:
    r = Rectangle(0, 5)
except InvalidSizeError as e:
    print(f"InvalidSizeError: {e}")