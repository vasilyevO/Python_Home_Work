# Одно слово
# Напишите программу, которая обрабатывает список из строк и удаляет все строки,
# содержащие более одного слова, а также преобразует оставшиеся строки к нижнему регистру.
#
# Данные:
# text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
# Пример вывода:
# Обработанный список: ['hello', 'world', 'simple']

import copy
print("Задание 1. Одно слово")
text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
deep_copy = copy.deepcopy(text_list)
for item in text_list:
    if len(item.split()) > 1:
        text_list.remove(item)
text_list = [item.lower() for item in text_list]
print("Начальный список:", deep_copy)
print("Обработанный список:", [item.lower() for item in text_list])

# Дан список товаров с ценами. Программа должна применить скидку к каждому товару и
# добавить в список элемент с новой ценой. В конце вывести таблицу с новой ценой.
# Данные:
#
# products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]
# Пример вывода:
#
# Введите скидку (в процентах): 17
#
# Товар          Старая цена    Новая цена
# Laptop            1200.00$       996.00$
# Mouse                25.00$         20.75$
# Keyboard           75.00$         62.25$
# Monitor            200.00$       166.00$

print("Задание 2. Изменение цены")
products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]
user_discount = int(input("Введите скидку (в процентах): "))
title = "Товар       |  Старая цена | Новая цена"
print(title)
print(len(title) * "-")

for i, (name, price) in enumerate(products):
    discount_price = round(price - (price * user_discount / 100), 2)
    products[i].append(discount_price)

for (name, price, new_price) in products:
    print(f"{name:<11} | {f'{price}$':^12} | {f'{new_price}$':>10}")
print()
print("Начальный список с новой ценой: ", products, sep="\n")



