# products = ["Молоко", "Хлеб", "Сахар-песок", "Подсолнечное масло", "Шоколадный батончик",
# "Мороженое"]
# print(*products, sep='\n')

# Task 2
# data = [("апельсин", 5), ("вишня", 12), ("киви", 18), ("ананас", 7), ("яблоко", 20)]
# print("Отфильтрованные данные:")
# for fruit, quantity in data:
#     if quantity > 10:
#        print(f"Товар : {fruit:<10} | Количество: {quantity:.2f}")

# products = [
#  ("Кофе", 127.99),
#  ("Чай", 52.49),
#  ("Шоколад", 81.99)
# ]
#
# discount = 17
# title = "Название    |   Цена    | Скидка   |Итоговая цена"
# print("Название    | Цена    | Скидка   |Итоговая цена")
# print(len(title) * "-")
#
# for item in products:
#     discount_price = item[1] * discount / 100
#     print(f"{item[0]:<11} | {item[1]:^7} | {discount:>7}% | {discount_price:<12.2f}")


# max_len = max(for item in products)
# print(max_len)

# products = [
#  ("Молоко", 3, 10),
#  ("Хлеб", 1, 5),
#  ("Сахар-песок", 2, 15),
#  ("Подсолнечное масло", 5, 3),
#  ("Шоколадный батончик", 4, 20),
#  ("Мороженое", 3, 20)
# ]
# title = "| Название |Цена | Количество|"
# max_leght1 = 0
#
# for item, price, quantity in products:
#     if len(item) > max_leght:
#         max_leght = len(item)
# title = f"| Название {(max_leght - 4) * " "} |    Цена | Количество |"
# print(title)
# print(len(title) * "-")
# for item in products:
#     print(f"| {item[0]:<{(max_leght + 5)}} | {item[1]:7.2f} | {item[2]:>10} |")




# Таблица покупок

# Напишите программу, которая обрабатывает список кортежей, где каждый кортеж
# содержит информацию о товаре: название, цена и количество.
# Выведите данные в формате таблицы, выровняв название по левому краю, а цену и
# количество — по правому.
# Учитывайте, что названия могут быть длинными. Выстраивайте выравнивание
# таблицы динамически, исходя их самого длинного названия товара.
# Данные:
# Python
products = [
("Молоко", 3000000000, 10000),
("Хлеб", 1, 5),
("Сахар-песок", 2, 15),
("Подсолнечное масло", 5, 3),
("Шоколадный батончик", 4, 20),
("Мороженое", 3, 20)
]

# print(len(title) * '-')
# max_len = len(max(products, key=len))
# print(max_len)
# lenth_1 = len(products[0])
# lenth_2 = 0
# lenth_3 = 0
#
# for product, price, q_ty in products:
#     if len(product) > lenth_1:
#         lenth_1 = len(product)
#     if len(str(price)) > lenth_2:
#         lenth_2 = len(str(price))
#         #print(lenth_2)
#     if len(str(q_ty)) > lenth_3:
#         lenth_3 = len(str(q_ty))
# title = f"| Название {(lenth_1 - 4) * ' '}|{(lenth_2) * ' '}Цена |{(lenth_3) * ' '}Количество |"
# print(title)
# print(len(title) * '-')
# for item in products:
#     print(f'| {item[0]:{(lenth_1 + 4)}} | {item[1]:{(lenth_2 + 3)}} | {item[2]:{(lenth_3 + 9)}} |')

# name_leng = 0
# products = [("Молоко", 3, 10), ("Хлеб", 1, 5), ("Сахар-песок", 2, 15), ("Подсолнечное масло", 5, 3), ("Шоколадный батончик", 4, 20), ("Мороженое", 3, 20)]
# for name, _, _ in products:
#     name_leng = max(name_leng, len(name))
# head = f'{'Название':{name_leng}} |{'Цена':5} | {"Количество":10}|'
# print(head, '-' * len(head), sep='\n')
# for name, price, amount in products:
#     print(f'{name:{name_leng}} |{price:5} | {amount:10}|')


# Число в конце
# Напишите программу, которая создает новый список. В него необходимо добавить только те строки
# из исходного списка, в которых цифры находятся только в конце.
# Данные:
# strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]
# Пример вывода:
# Строки с цифрами только в конце: ['apple23', 'grape3']

strings = ["apple123", "ban1ana45", "12cherry", "grape3", "blue23berry"]
dig_string = []
for item in strings:
    if item and item[-1].isdigit():
        dig_string.append(item)
print("Строки с цифрами только в конце: ", dig_string)

strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]
print(strings)
new_strings = []
for x in strings:
    if x[len(x) - 1].isdigit():
        new_strings.append(x)
print(new_strings)

strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]
new_strings = []
for item in strings:
    if item.rstrip("0123456789").isalpha():
        new_strings.append(item)
print("Строки с цифрами только в конце: ", new_strings)


# Напишите программу, которая удаляет из списка все значения, кратные числу, которое вводится пользователем.
# Данные:
# numbers = [1, 3, 6, 9, 10, 12, 15, 19, 20]
# Пример вывода:
# Введите число для удаления кратных ему элементов: 3
# Список без кратных значений: [1, 10, 19, 20]

numbers = [1, 3, 6, 9, 10, 12, 15, 19, 20]
num1 = int(input("Введите число для удаления кратных ему элементов: "))
new_list = []
for item in numbers:
    if item % num1:
       new_list.append(item)
print("Список без кратных значений: ", new_list)

# Напишите программу, которая формирует новый список чисел. Добавьте в него все элементы исходного списка, где:
# нечетные числа занимают те же позиции,
# чётные числа отсортированы между собой обратном порядке.
# Данные:
# numbers = [5, 2, 3, 8, 4, 1, 2, 7]
# Пример вывода:
# Список после сортировки: [5, 8, 3, 4, 2, 1, 2, 7]

numbers = [5, 2, 3, 8, 4, 1, 2, 7]
new_list = []
for item in numbers:

y = [list(x[0]) for _ in range(5)] # это глубокое копирование, когда нужны разные ссылки на элементы