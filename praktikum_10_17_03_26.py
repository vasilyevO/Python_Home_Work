"""
Реализуйте функцию, которая принимает любое количество строк с текстом.
Функция должна возвращать подсчет самых популярных слов в количестве,
переданном в функцию. Программа должна игнорировать регистр слов. Выведите 5
самых популярных слов и их количество.
Данные:
text1 = "This is a sample text with some repeated words."
text2 = "Another sample text with different words."
text3 = "Text processing is fun when words repeat."
"""

# text1 = "This is a sample text with some repeated words."
# text2 = "Another sample text with different words."
# text3 = "Text processing is fun when words repeat."
#
# from collections import Counter
#
# def count_words(*texts, quantity = 5):
#     all_words = []
#     for text in texts:
#         text = text.lower().replace(".", " ").split()
#         all_words.extend(text)
#     counter = Counter(all_words)
#     return counter.most_common(quantity)
#
# quantity = input("Введите количество слов: ")
# # print(f"{quantity} самых популярных слов:")
# top_words = count_words(text1, text2, text3, quantity)
# # for word, count in top_words:
# #     print(f"{word}: {count}")
#
# print(f"{quantity} самых популярных слов:\n" + "\n".join(f"{word}: {count}" for word, count in top_words))
"""

Группировка задач по категории
Реализуйте функцию, которая принимает словарь задач с категориями и группирует
задачи по их категориям.

Данные:
Python
Unset
Python
tasks = {
 "task1": "работа",
 "task2": "учёба",
 "task3": "развлечения",
 "task4": "работа",
 "task5": "учёба"
}

Пример вывода:
Группировка по категориям:
{
 'работа': ['task1', 'task4'],
 'учёба': ['task2', 'task5'],
 'развлечения': ['task3']
}
"""

tasks = {
 "task1": "работа",
 "task2": "учёба",
 "task3": "развлечения",
 "task4": "работа",
 "task5": "учёба"
}

from collections import defaultdict
def group_tasks(tasks):
    new_dict = defaultdict(list)
    for task, category in tasks.items():
        new_dict[category].append(task)
    return new_dict
print(group_tasks(tasks))


def group_tasks(tasks):
    grouped = {}
    for task, category in tasks.items():
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(task)
    return grouped

"""
Поиск задач
Реализуйте функцию, которая принимает словарь задач с категориями и нужную
категорию. Функция должна возвращать список задач для указанной категории.
Данные:
tasks = {
 "task1": "работа",
 "task2": "учёба",
 "task3": "развлечения",
 "task4": "работа",
 "task5": "учёба"
}
category = "учёба"
Пример вывода:
Задачи для категории 'учёба':
['task2', 'task5'
"""

tasks = {
 "task1": "работа",
 "task2": "учёба",
 "task3": "развлечения",
 "task4": "работа",
 "task5": "учёба"
}

# from collections import defaultdict
# def group_tasks1(tasks, category):
#
#     return [task for task, cat in tasks.items() if cat == category]
# print(group_tasks1(tasks, "учёба"))
#
# def ordered_tasks(tasks):
#     keys_to_end = [key for key, value in tasks.items() if "низкий" in value]
#     keys_to_start = [key for key, value in tasks.items() if "высокий" in value]
#     for key in keys_to_end:
#         tasks.move_to_end(key)
#     for key in keys_to_start:
#         tasks.move_to_end(key, last=False)
#     return tasks
# print(f"Очередь задач: {ordered_tasks(tasks)}")
#
# #если интересно, так тоже работает
# l = lambda word : (
#     print(word) or word.lower()
# )
# print(l("AAA"))

"""
Простое число
Напишите функцию, которая проверяет, является ли число n простым (делится только на 1 и само себя) и возвращает булевый результат.
Данные:
n = 17
Пример вывода:
Число 17 является простым
"""
n = 17
def prost_chisl(value):
    return value / 1 and