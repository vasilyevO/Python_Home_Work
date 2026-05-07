print("\n 1. Класс Rectangle")
class Rectangle:
    """A class that describes a rectangle."""

    def __init__(self, width: float, height: float) -> None:
        """
        Initialises a rectangle with the specified width and height.

        Args:
            width: width of the rectangle.
            height: the height of the rectangle.
        """
        self.width = width
        self.height = height

    def get_area(self) -> float:
        """Returns the area of a rectangle."""
        return self.width * self.height

rect = Rectangle(5, 4)
print(f"Площадь: {rect.get_area()}")

rect.width = 7
rect.height = 5
print(f"Новая площадь: {rect.get_area()}")


print("\n 2. Класс Counter")
class Counter:
    """A simple counter with increment and decrement methods."""

    def __init__(self) -> None:
        """Initialises the counter to zero."""
        self.value = 0

    def increment(self) -> None:
        """Increases the counter by 1 and displays the current value."""
        self.value += 1
        print(f"Значение увеличено, текущее: {self.value}")

    def decrement(self) -> None:
        """Decreases the counter by 1 and displays the current value."""
        self.value -= 1
        print(f"Значение уменьшено, текущее: {self.value}")

    def get_value(self) -> int:
        """Returns the current value of the counter."""
        return self.value

counter = Counter()
counter.increment()
counter.increment()
counter.increment()
counter.decrement()
print(f"Текущее значение: {counter.get_value()}")