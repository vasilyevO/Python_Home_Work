# Одно слово
# Напишите программу, которая обрабатывает список из строк и удаляет все строки,
# содержащие более одного слова, а также преобразует оставшиеся строки к нижнему регистру.
#
# Данные:
# text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
# Пример вывода:
# Обработанный список: ['hello', 'world', 'simple']

print("Задание 1. Одно слово")
text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
new_list = []
for item in text_list:
    if len(item.split()) > 1:
        continue
    new_list.append(item.lower())
print("Начальный список:", text_list)
print("Обработанный список:", new_list)

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
    discount_price = price - (price * user_discount / 100)
    products[i][1] = round(discount_price, 2)
    print(f"{name:<11} | {f'{price}$':^12} | {f'{discount_price:.2f}$':<10}")
print("Начальный список с новой ценой: ", products, sep="\n")



