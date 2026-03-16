"""
1. Реверс словаря
Напишите программу, которая меняет местами ключи и значения в словаре.
Если значения повторяются, добавьте их в список.

Данные:
data = {"a": 1, "b": 2, "c": 1, "d": 3}

Пример вывода:
Перевернутый словарь: {1: ['a', 'c'], 2: ['b'], 3: ['d']}
"""
print("1. Реверс словаря")
data = {"a": 1, "b": 2, "c": 1, "d": 3}
inverted_dict = {}

for key, value in data.items():
    if value not in inverted_dict:
        inverted_dict[value] = [key]
    else:
        inverted_dict[value].append(key)

print("Инверсированный словарь:", inverted_dict)

"""
2. Счётчик букв в словах
Напишите программу, которая подсчитывает количество каждой буквы в заданных словах и создаёт словарь, 
где ключи — это слова, а значения — это ещё один словарь с подсчётом каждой буквы.

Данные:
words = ["anna", "bennet", "john"]

Пример вывода:
{'anna': {'a': 2, 'n': 2}, 'bennet': {'b': 1, 'e': 2, 'n': 2, 't': 1}, 'john': {'j': 1, 'o': 1, 'h': 1, 'n': 1}}
"""
print("\n 2. Счётчик букв в словах")
words = ["anna", "bennet", "john"]
data = dict()
for word in words:
    data[word] = {x : word.count(x) for x in set(word)}
print(data)

print("\n 2. Счётчик букв в словах через метод Counter")
# через метод Counter и обычный словарь dict
from collections import Counter
words = ["anna", "bennet", "john"]
result = {word: dict(Counter(word)) for word in words}
print(result)

# 3. Распределение студентов по группам
print("\n 3. Распределение студентов по группам")
students = {"Аня": 92, "Боря": 76, "Ваня": 65, "Галя": 48, "Дима": 88, "Ева": 54}
groups = ["Отличники", "Хорошисты", "Троечники", "Не сдали"]

result = {group: {} for group in groups}

for name, score in students.items():
    if score >= 85:
        group_name = "Отличники"
    elif score >= 70:
        group_name = "Хорошисты"
    elif score >= 50:
        group_name = "Троечники"
    else:
        group_name = "Не сдали"

    result[group_name][name] = score

print(result)