# Home work 13
#Исправленное задание 2

# Прогрессия увеличения
# numbers = (3, 7, 2, 8, 5, 10, 1)
# result = (numbers[0],)
# max_value = numbers[0]
#
# for num in numbers[1:]:
#     if num > max_value:
#         result += (num,)
#         max_value = num

print("1. Прогрессия увеличения.")
numbers = (3, 7, 2, 8, 5, 10, 1)
print("Исходные значения: ", numbers)
result = [numbers[0]]
max_value = numbers[0]

for num in numbers[1:]:
    if num > max_value:
        result.append(num)
        max_value = num

print("Кортеж по возрастанию:", tuple(result))

print("2. Повторяющиеся элементы.")
numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)
checked = []
for value in numbers:
    if value not in checked and numbers.count(value) > 1:
        checked.append(value)
        indexes = []

        for index, item in enumerate(numbers):
            if item == value:
                indexes.append(index)

        print(f"Индексы элемента {value}:", *indexes)