print("\n 1. Среднее время выполнения")
import time
from typing import Callable

def measure_time(func: Callable) -> Callable:
    """
    A decorator that measures the average execution time of a function over five calls.

    Args:
        func: decorative feature.

    Returns:
        Inverse function with measurement of average execution time.
    """
    def wrapper(*args, **kwargs) -> None:
        """Calls the function 5 times and displays the average execution time."""
        times = []
        for _ in range(5):
            start = time.time()
            func(*args, **kwargs)
            end = time.time()
            times.append(end - start)

        avg = sum(times) / len(times)
        print(f"Среднее время выполнения: {avg:.3f} сек")

    return wrapper

@measure_time
def compute() -> int:
    """Sums numbers from 0 to 10,000,000."""
    total = 0
    for i in range(10_000_000):
        total += i
    return total

compute()


print("\n 2. Среднее время выполнения с количеством вызовов")
import timeit
from typing import Callable

def measure_time(repeats: int) -> Callable:
    """
    A decorator with a parameter — measures the average execution time of a function.

    Args:
        repeats: number of function calls.

    Returns:
        A decorator that measures the average time and displays the result.
    """
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> None:
            result = None

            def call():
                nonlocal result
                result = func(*args, **kwargs)

            total = timeit.timeit(call, number=repeats)
            avg = total / repeats
            print(f"Среднее время выполнения для {repeats} вызовов: {avg:.2f} секунд")
            print(f"Результат: {result}")

        return wrapper
    return decorator

@measure_time(repeats=10)
def compute() -> int:
    """Sums numbers from 0 to 10,000,000."""
    total = 0
    for i in range(10_000_000):
        total += i
    return total
compute()

