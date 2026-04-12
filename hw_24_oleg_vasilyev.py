
print("\n 1. Сумма цифр числа")
def sum_digits(n: int) -> int:
    """
     Recursively calculates the sum of the digits of an integer.

    :param n: Integer (positive).
    :param return: sum of its digits.
    """
    if n < 10:
        return n

    return n % 10 + sum_digits(n // 10)

num = 43197
print(f"Сумма цифр числа {num}: {sum_digits(num)}")


print("\n 2. Сумма вложенных чисел")
from typing import List, Any

def sum_nested(data: List[Any]) -> int:
    """
    Recursively sums all the numbers in the nested lists.

    :param data: A list containing numbers or other lists.
    :return: The total sum of all the numbers found.
    """
    total = 0
    for item in data:
        if isinstance(item, list):
            total += sum_nested(item)
        else:
            total += item
    return total

nested_numbers = [1, [2, 3], [4, [5, 6]], 7]
result = sum_nested(nested_numbers)

print(f"Результат вычислений: {result}")

