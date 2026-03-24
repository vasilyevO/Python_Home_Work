# # Задание 1
#
# for task in range(1, 4):
#     match task:
#         case 1:
#             print("1.Таблица умножения")
#             number =  int(input("Введите число: "))
#             for i in range(1, number + 1):
#                 for j in range(1, number + 1):
#                     print(i * j, end="\t")
#                 print()
#
# # Задание 2
# print("2.Лестница чисел")
# number = int(input("Введите число: "))
# for row in range(1, number + 1):
#     for line in range(1, row + 1):
#         print(line, end=" ")
#     print()
#
# # Задание 3
# print("3.Удаление всех повторяющихся символов")
# string = input("Введите строку: ")
#             result = ""
#             for char in string:
#                 if char not in result:
#                     result += char
#             print(result)



# x = "PythonPython"
#
# y = set(x)
# print(y)
#
# x = "PythonPython"
#
# y = sorted(set(x))
# print(y)
#
# # Вводим строку получаем список для обращения к каждому элементу
# x = list("Python")
# print(x)
#
# # Когда нужно получить последовательность от и до введенного числа.
# x = list(range(10))
# print(x)
#
# digits = list(input('number> '))
# print(digits)
#
# my_list = [10, 20, 30, 40, 50, 70]
# my_list[1::2] = [200] * 5
# print(my_list)


# HW 10
# Task 10

# my_list = [50, 10, 5, 2, 1]
# price = int(input('Введите стоимость товара: '))
# for item in my_list:
#     if item > price:
#         item %= price
#         print(item)
#         int_part

# print("1.Торговый автомат")
# price = int(input("Введите стоимость товара: "))
weight = [50, 10, 5, 2, 1]
# for coin in weight:
#     int_part = price // coin
#     if int_part:
#         print(f"Внесите монеты номиналом {coin}:", int_part)
#         price %= coin
#


# number = int(input("Введите число: "))
# row = 1
# column = 1
#
# for i in range(1000):
#     print(column, end=" ")
#     column += 1
#
#     if column > row:
#         print("\n", end="")
#         row += 1
#         column = 1
#
#     if row > number:
#         break


# cost = int(input("Введите стоимость товара: "))
# funfzig = cost//50
# zehn = (cost-(50*funfzig))//10
# funf = (cost-(10*zehn+50*funfzig))//5
# zwei = (cost-(5*funf+10*zehn+50*funfzig))//2
# print(f"Внесите монеты номиналом 50: {funfzig}",
#       f"Внесите монеты номиналом 10: {zehn}",
#       f"Внесите монеты номиналом 5: {funf}",
#       f"Внесите монеты номиналом 2: {zwei}",
#       sep="\n")




fruits = ['apple', 'banana', 'cherry']
text = "".join(fruits)
print(text)