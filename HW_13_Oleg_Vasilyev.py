# Home work 13

# Прогрессия увеличения
numbers = (3, 7, 2, 8, 5, 10, 1)
result = (numbers[0],)
max_value = numbers[0]

for num in numbers[1:]:
    if num > max_value:
        result += (num,)
        max_value = num

print("Кортеж по возрастанию:", result)

# 2. Повторяющиеся элементы
numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)
checked = ()

for value in numbers:
    if value not in checked and numbers.count(value) > 1:
        indexes = ()
        for index, item in enumerate(numbers):
            if item == value:
                indexes += (index,)

        print(f"Индекс элемента {value}: {indexes}")
        checked += (value,)