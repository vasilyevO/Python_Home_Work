print("\n 1. План по дням недели")

from itertools import cycle

weekly_schedule: dict[str, list[str]] = {
    "Monday": ["Gym", "Work", "Read book"],
    "Tuesday": ["Meeting", "Work", "Study Python"],
    "Wednesday": ["Shopping", "Work", "Watch movie"],
    "Thursday": ["Work", "Call parents", "Play guitar"],
    "Friday": ["Work", "Dinner with friends"],
    "Saturday": ["Hiking", "Rest"],
    "Sunday": ["Family time", "Rest"]
}

def run_planner_cycle(schedule: dict[str, list[str]]) -> None:
    """
    Launches a scheduler based on the cycle generator.
    Displays the schedule for the following day each time Enter is pressed.
    Stops when 'q' is entered.

    Args:
        schedule: a dictionary with a weekly timetable.
    """
    day_cycle = cycle(schedule.items())

    while True:
        day, tasks_list = next(day_cycle)
        tasks: str = ", ".join(tasks_list)
        print(f"{day}: {tasks}")

        if input("Нажмите Enter для продолжения (q — выход): ") == "q":
            break

run_planner_cycle(weekly_schedule)


print("\n 2. Объединение списков продуктов")
from typing import Iterator

fruits = ["Apple", "Banana", "Orange"]
vegetables = ["Carrot", "Tomato", "Cucumber"]
dairy = ["Milk", "Cheese", "Yogurt"]


def combine_products(*args: list[str]) -> Iterator[str]:
    """
    Takes several lists of products and returns an iterator that
    contains all the products in lower case.

    Args:
        *args: any number of lists containing product names.

    Returns:
        Lowercase string generator.
    """
    for product_list in args:
        for product in product_list:
            yield product.lower()


gen = combine_products(fruits, vegetables, dairy)

for product in gen:
    print(product)


print("\n 3. Комбинации одежды")
from itertools import product
from typing import Iterator

clothes = ["T-shirt", "Jeans", "Jacket"]
colors = ["Red", "Blue", "Black"]
sizes = ["S", "M", "L"]

def clothing_combinations(
    clothes: list[str],
    colors: list[str],
    sizes: list[str]
) -> Iterator[str]:
    """
    Generates all possible combinations of clothing, colours and sizes.

    Args:
        clothes: a list of clothing types.
        colors: list of colours.
        sizes: size chart.

    Returns:
        String generator in the format "Clothe - Color - Size".
    """
    for clothe, color, size in product(clothes, colors, sizes):
        yield f"{clothe} - {color} - {size}"

gen = clothing_combinations(clothes, colors, sizes)

for combination in gen:
    print(combination)