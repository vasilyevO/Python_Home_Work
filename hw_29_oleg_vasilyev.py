print("\n 1. Генератор Фибоначчи")

from typing import Iterator
from itertools import islice

def fibonacci() -> Iterator[int]:
    """
    An infinite Fibonacci sequence generator.

    Yields:
        The Fibonacci numbers, one by one, starting with 0.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fibonacci()

for item in islice(gen, 10):
    print(item)

print("\n 2. Генератор уникальных элементов")

from typing import Iterator
data = [3, 1, 2, 3, 4, 1, 5, 2, 6, 7, 5, 8]

def unique_elements(data: list[int]) -> Iterator[int]:
    """
    A generator of unique elements that preserves the order.

    Args:
        data: a list of items, which may contain duplicates.

    Yields:
        Unique elements listed in order of first appearance.
    """
    seen = set()
    for item in data:
        if item not in seen:
            yield item
            seen.add(item)

gen = unique_elements(data)
for item in gen:
    print(item)