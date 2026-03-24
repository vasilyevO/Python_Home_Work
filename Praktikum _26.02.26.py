# Дан текст. Программа должна:
# ● Разбить текст на слова.
# ● Создать список уникальных слов в алфавитном порядке (не учитывая регистр).
# ● Вывести количество уникальных слов.
# Данные:
# text = "Python is a great programming language. Python is popular and powerful."
# Пример вывода:
# Количество уникальных слов: 9
# Уникальные слова: ['a', 'and', 'great', 'is', 'language', 'popular', 'powerful', 'programming',
# 'python']

# text = "Python is a great programming language. Python is popular and powerful."
# text = text.lower().split()
# text_for_check = []
#
#
# for word in text:
#     if word not in text_for_check:
#         print(word, end=', ')
#     text_for_check.append(word)

# task 3
# Самое длинное слово
# Дано предложение. Найдите самое длинное слово и выведите это слово с его длиной.
# Данные:
# sentence = "Programming in Python is both fun and educational"
# Пример вывода:
# Самое длинное слово: Programming
# Длина слова: 11

# sentence = "Programming in Python is both fun and educational"
# sentence_sort = sentence.lower().split()
#
# longer_words = max(sentence_sort, key=len)
# print("Самое длинное слово:", longer_words)
# print("Длина слова:", len(longer_words))


# 5
# Перемещение в конец
# Напишите программу, которая перемещает все элементы списка, меньше 5, в конец списка, сохраняя порядок
# остальных элементов.
# Данные:
# numbers = [4, 7, 1, 6, 3, 8, 2]
# Пример вывода:
# Перемещённые элементы: [6, 7, 8, 4, 1, 3, 2]

numbers = [4, 7, 1, 6, 3, 8, 2]
for item in numbers:
    if item <= 5:
        numbers.remove(item)
        numbers.append(item)

print("Перемещенные элементы:", numbers)

# 5
# Суммы пар
# Напишите программу, которая обрабатывает список чисел и возвращает новый список, содержащий все
# возможные суммы пар разных элементов без дубликатов значений. Результат должен быть отсортирован по
# убыванию.
# Данные:
# numbers = [3, 5, 9]
# Пример вывода:
# Суммы пар чисел по убыванию: [14, 12, 8]

numbers = [3, 5, 9]
sums = []
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if j not in sums:
            sums.append(numbers[i] + numbers[j])

result = sorted(sums, reverse=True)

print(f"Суммы пар чисел по убыванию: {result}")


# Покупки с лимитом бюджета
# Дан список покупок, где каждый элемент — это кортеж с названием товара и его ценой. Покупки
# распределены по приоритетности. Пользователь вводит бюджет. Программа должна вывести:
# ● список покупок, которые он может себе позволить;
# ● итоговую стоимость этих товаров.
# Данные:
# shopping_list = [
#  ("Bread", 1.20),
#  ("Milk", 0.99),
#  ("Eggs", 2.50),
#  ("Butter", 3.75),
#  ("Cheese", 4.10),
#  ("Apple", 0.50)
# ]
# Пример вывода:
# Введите ваш бюджет: 7
# Покупки в рамках бюджета:
# Bread: $1.20
# Milk: $0.99
# Eggs: $2.50
# Apple: $0.50
# Итоговая стоимость: $5.19

# input_budget = 7
# shopping_list = [
#  ("Bread", 1.20),
#  ("Milk", 0.99),
#  ("Eggs", 2.50),
#  ("Butter", 3.75),
#  ("Cheese", 4.10),
#  ("Apple", 0.50)]
#
# total = 0
# for product, price in shopping_list:
#     if input_budget > price:
#         input_budget -= price
#         total += price
#         print(product, ":", price)
# print(f"Итоговая стоимость: {total:.2f}")


# Упаковка товаров по ящикам
# У вас есть список весов товаров. Каждый ящик может выдержать не более заданного веса. Напишите
# программу, которая распределяет товары по минимальному количеству ящиков, не превышая допустимый
# вес.
# Данные:
# weights = [3, 4, 9, 8, 2, 5, 3, 6, 1, 7, 1, 1, 2, 4]
# Пример вывода:
# Введите максимальный вес ящика:
# 10
# Распределение по ящикам:
# Ящик 1: [9, 1]
# Ящик 2: [8, 2]
# Ящик 3: [7, 3]
# Ящик 4: [6, 4]
# Ящик 5: [5, 4, 1]
# Ящик 6: [3, 2, 1]


# weights = [3, 4, 9, 8, 2, 5, 3, 6, 1, 7, 1, 1, 2, 4]
# kg_in_box = 10 #int(input("Enter kg in box: "))
# box = []
# sum_in_box = 0
#
# for weight in weights:
#     if sum_in_box + weight >= kg_in_box:
#         print(box)
#         box.clear()
#         sum_in_box = 0
#     box.append(weight)
#     sum_in_box += weight



weights = [3, 4, 9, 8, 2, 5, 3, 6, 1, 7, 1, 1, 2, 4]

max_weight = int(input("Введите максимальный вес ящика: "))

# Сортируем по убыванию
weights.sort(reverse=True)

boxes = []

for weight in weights:
    placed = False

    # Пробуем положить в существующие ящики
    for box in boxes:
        if sum(box) + weight <= max_weight:
            box.append(weight)
            placed = True
            break

    # Если не поместился — создаём новый ящик
    if not placed:
        boxes.append([weight])

print("Распределение по ящикам:")
for i, box in enumerate(boxes, 1):
    print(f"Ящик {i}: {box}")