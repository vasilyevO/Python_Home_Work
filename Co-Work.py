

# print("Задание 1. Звёздочки вместо чисел.")
# text = "My number is 123-456-789"
# for char in text:
#     if char.isdigit():
#         text = text.replace(char, str("*"))
# print(text)

# print("Задание 2. Количество символов.")
# text = "Programming in python"
# print("Строка:", text)
# for char in text.casefold():
#     print(f"Символ '{char}' встречается {text.count(char)} раз(а)") if text.count(char) > 1 else None
#     text = text.replace(char, "")

# Вариант 2:
# print("Задание 2. Количество символов.")
#
# text = "Programming in python".casefold()
# printed = ""
# print("Строка:", text)
#
# for char in text:
#     if char in printed:
#         continue
#     count = text.count(char)
#     if count > 1:
#         print(f"Символ '{char}' встречается {count} раз(а)")
#         printed += char


# Увеличение чисел
# Напишите программу, которая заменяет все числа в строке на их эквивалент, умноженный на 10.
# text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
# Пример вывода:
# I have 50.0 apples and 100.0 oranges, price is 5.0 each. Card number is ....3672.

# text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
# new_symbols = []
# for char in text.split():
#     if char.count('.') <= 1 and char.replace('.', '').isdigit():
#          char = str(float(char) * 10)
#     new_symbols.append(char)
# new_text = " ".join(new_symbols)
# print(new_text)

# Домашка №11 п.3 "Увеличение чисел" одной строкой (если интересно)
# Домашка №11 п.3 "Увеличение чисел" одной строкой (если интересно)
# print(" ".join([str(int(x) * 10) if x.isdigit() else str(float(x) * 10) if len(
#     x.split(".")) == 2 and x.split(".")[0].isdigit() and x.split(".")[1].isdigit() else x for x in
#                "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672.".split()]))
# text = []
# for x in "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672.".split():
#
#     if x.isdigit():
#         text += [str(int(x) * 10)]
#     elif len(x.split(".")) == 2 and x.split(".")[0].isdigit(): and x.split(".")[1].isdigit():
#              text += [str(float(x) * 10)]
#     else:
#         text += [x]
# print(" ".join(text))
#
# y = "05"
# print(y.split(".")[0].isdigit())

# my_tuple = (1, 2, 4, "apple", True)
# print(my_tuple)
# print(my_tuple[-1])


# numbers = [10, 3, 7, 1]
#
# minimum = numbers[0]
#
# for n in numbers:
#     if n < minimum:
#         minimum = n
#
# print(minimum)

nested_list = [1, 2, 3]
nested_list.insert(2, [4, 5])
print(nested_list)