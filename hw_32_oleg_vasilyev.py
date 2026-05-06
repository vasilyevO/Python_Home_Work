print("\n 1. Фабрика функций округления")

from typing import Callable
def make_rounder(digits: int) -> Callable[[float], float]:
    """
    The Rounding Function Factory.

    Args:
        digits: the number of decimal places.

    Returns:
        A function that rounds a number to *digits* decimal places.
    """
    def rounder(number: float) -> float:
        """Rounds the number to a specified number of decimal places."""
        return round(number, digits)
    return rounder

round2 = make_rounder(2)
round0 = make_rounder(0)

print(round2(3.14159))
print(round2(2.71828))
print(round0(9.999))


print("\n 2. Расширяемый логгер событий")
from datetime import datetime
from typing import Callable

def make_logger() -> Callable:
    """
    Creates an event logger that stores the history in the short-circuit.

    Returns:
        A logger function that records events along with their timestamps
        and returns the entire list when called without any arguments.
    """
    events: list[str] = []

    def logger(event: str = None) -> list[str] | None:
        """
        Saves an event or returns all events.

        Args:
            event: event name. If None, returns the entire list.

        Returns:
            A list of all events if `event` is not provided; otherwise, `None`.
        """
        if event is None:
            return events
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        events.append(f"{event}: {timestamp}")

    return logger

log = make_logger()
log("Загрузка данных")
log("Обработка завершена")
log("Сохранение файла")

for event in log():
    print(event)

print("\n 3. Рамка вокруг вывода.")
from typing import Callable
def frame(func: Callable) -> Callable:
    """
    A decorator that wraps the function's output in a frame of 50 '-' characters.

    Args:
        func: decorative feature.

    Returns:
        An inverted function with a frame before and after the output.
    """
    def wrapper(*args, **kwargs) -> None:
        """Calls func between the two separator lines."""
        print("-" * 50)
        func(*args, **kwargs)
        print("-" * 50)
    return wrapper

@frame
def say_hello(name: str) -> None:
    """Welcomes the player."""
    print(f"Привет, {name}!")

say_hello("игрок")