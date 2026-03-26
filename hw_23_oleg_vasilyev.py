

print("\n 1. Объединение данных в строку")

from typing import Any
data = [42, "hello", [1, 2, 3], {"a": 1, "b": 2}]

def join_data(data_list: list[Any]) -> str:
    """
    Converts list items into strings and concatenates them using ' | '.

    :param data_list: A list of items of any type.
    :return: A line with items separated by a vertical line.
    """

    string_elements = [str(item) for item in data_list]
    return " | ".join(string_elements)

print(join_data(data))


print("\n 2. Сумма вложенных чисел")
from functools import reduce
from typing import List, Dict, Any

data = [
    {"name": "Alice", "scores": [10, 20, 30]},
    {"name": "Bob", "scores": [5, 15, 25]},
    {"name": "Charlie", "scores": [7, 17, 27]}
]

def get_total_score(data: List[Dict[str, Any]]) -> int:
    """
    Calculates the total score of all users in the list.

    :param data: List of dictionaries containing names and marks.
    :return: Total score of all students.
    """
    user_sums = map(lambda user: sum(user["scores"]), data)
    return reduce(lambda a, b: a + b, user_sums)

print(f"Итоговый балл: {get_total_score(data)}")

