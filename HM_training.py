# numbers = [[1], [2], [3]]
#
# for i in range(len(numbers)):
#     numbers[i] = [0]
#
# print(numbers)

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

string = "({[}])"


# Задача со скобками
print("Скобки:", string)

stack = []  # создаём пустой список (наш стек)
valid = True  # предполагаем, что строка правильная

for ch in string:  # перебираем каждый символ строки

    # 1️⃣ Если открывающая скобка — добавляем в стек
    if ch == "(" or ch == "[" or ch == "{":
        stack.append(ch)

    # 2️⃣ Если закрывающая — проверяем
    elif ch == ")" or ch == "]" or ch == "}":

        # если стек пуст — закрывать нечего
        if len(stack) == 0:
            valid = False
            break

        last = stack.pop()  # достаём последнюю открытую

        # проверяем соответствие
        if ch == ")" and last != "(":
            valid = False
            break
        elif ch == "]" and last != "[":
            valid = False
            break
        elif ch == "}" and last != "{":
            valid = False
            break

# После цикла проверяем — не осталось ли открытых
if len(stack) != 0:
    valid = False

print("Валидны:", valid)