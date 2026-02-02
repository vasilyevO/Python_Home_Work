# # One branch
# t = int(input('T>>'))
#
# if t < 0:
#     print('Hello')
#     print('It is cold!')
#
#
# print('Have a nice day!')

# name = input("Enter your name: ")
#
# if len(name) > 0: # BAD STYLE
#     print(name.upper())
#
# if name: # COOL STYLE
#     print(name.upper())


# # Two branches
# t = int(input('T>'))
#
# if t < 0:
#     print('It is cold')
# else:
#     print('It is normal')
#
# print('Have a  nice day!')

#
# number = int(input("Enter a number: "))
#
# # BAD STYLE
# if number % 2 == 0:
#     print("even")
# else:
#     print("odd")
#
#
# # GOOD STYLE
# if number % 2:
#     print("odd")
# else:
#     print("even")


# t = int(input('T>'))
#
# if t > 10:
#     money = float(input('Money>'))
#     if money > 100:
#         print('Go to shopping')
#     else:
#         print('Not enough money')
# else:
#     print('Bad weather')


#
# salary = int(input('Enter your salary: '))
#
# # BAD
# if salary <= 1000:
#     print('Taxes = 10%')
# else:
#     if salary < 2000:
#         print('Taxes = 20%')
#     else:
#         if salary <= 4000:
#             print('Taxes = 40%')
#         else:
#             print('Taxes = 50%')
#
#
# if salary <= 1000:
#     print('Taxes = 10%')
# elif salary < 2000:
#     print('Taxes = 20%')
# elif salary <= 4000:
#     print('Taxes = 40%')
# else:
#     print('Taxes = 50%')



# a = 10
# if a == 10:
#     print(10)
#     a = 0
# elif a == 0:
#     print(0)
#     a = 100
# elif a == 200:
#     print(200)
# else:
#     print(a)
#
# print(a)

#
# a = 10
# if a == 10:
#     print(10)
#     a = 0
# if a == 0:
#     print(0)
#     a = 100
# if a == 200:
#     print(200)
# else:
#     print(a)
#
# print(a)
#


# salary = 1000
#
# if salary <= 1000:
#     print('Taxes = 10%')
# elif salary < 2000:
#     print('Taxes = 20%')
# elif salary <= 4000:
#     print('Taxes = 40%')
# else:
#     print('Taxes = 50%')



# if salary <= 1000:
#     print('Taxes = 10%')
#
# if salary < 2000:
#     print('Taxes = 20%')
#
# if salary <= 4000:
#     print('Taxes = 40%')
# else:
#     print('Taxes = 50%')


# t = int(input('T>>'))
# money = float(input('Money>>'))
#
# # BAD
# if t > 10:
#     if money > 100:
#         print('Shopping')
#
# # GOOD
# if t > 10 and money > 100:
#     print('Shopping')


# points = float(input("Enter a number: "))
#
# if points < 0 or points > 100:
#     print("Invalid number")
# elif points < 60:
#     print('F')
# elif points < 70:
#     print('E')
# elif points < 75:
#     print('D')
# elif points < 80:
#     print('C')
# elif points < 90:
#     print('B')
# else:
#     print('A')



# salary = int(input('Enter your salary: '))
# # 4 lines, 2 branches, 1 var, simple expr
# if salary < 4000:
#     taxes = 0.25
# else:
#     taxes = 0.5
#
# print('Tax rate:', taxes)
# netto = salary * (1 - taxes)
# print('Netto:', netto)
#
#
#
# # taxes = 0.25 if salary < 4000 else 0.5
# # print('Tax rate:', taxes)
#
# netto = (1 - 0.25 if salary < 4000 else 0.5) * salary
# print('Netto:', netto)

# a, b, c = int(input('Enter 1-st number: ')),\
#                    int(input('Enter 2-nd number: ')), \
#                    int(input('Enter 3-nd number: '))
# if a <= b and b <= c:
#     print("Числа в порядке возрастания:", a, b, c, sep=",")
# elif a <= c and c <= b:
#     print("Числа в порядке возрастания:", a, c, b, sep=",")
# elif b <= a and a <= c:
#     print("Числа в порядке возрастания:", b, a, c, sep=",")
# elif b <= c and c <= a:
#     print("Числа в порядке возрастания:", b, c, a, sep=",")
# elif c <= a and a <= b:
#     print("Числа в порядке возрастания:", c, a, b, sep=",")
# else:  # c <= b <= a
#     print("Числа в порядке возрастания:", c, b, a, sep=",")



# year = int(input('Enter the year: '))
# res = "The year is a leap year" if year % 4 else "Хорошо" if score > 75 else
# "Удовлетворительно" if score > 50 else "Неудовлетворительно"
#
# if year % 4 and year % 400 and year % 100:
#         print("The year is not a leap year.")
# else:
#     print("The year is a leap year.")

# year = int(input("Введите год: "))
## if year % 4:
#     print("Год не является високосным.")
# elif year % 100 == 0 and year % 400 != 0:
#     print("Год не является високосным.")
# else:
#     print("Год является високосным.")

# year = int(input("Введите год: "))
#
# if year % 4: # Остаток при делении на 4 есть -> не делится -> то, не високосный
#     print("Год не является високосным.")
# elif year % 100: # Остаток при делении на 100 есть -> не делится -> то, високосный
#     print("Год является високосным.")
# elif year % 400: # Остаток при делении на 400 есть -> не делится -> то, не високосный
#         print("Год не является високосным.")
# else:
#     # Все остальные случаи -> високосный
#     print("Год является високосным.")

# Practikum

# 1
# Упорядочить числа по возрастанию
# Напишите программу, которая принимает три числа и определяет, являются ли они упорядоченными по
# возрастанию.

# a, b, c = int(input('Enter 1-st number: ')),\
#                    int(input('Enter 2-nd number: ')), \
#                    int(input('Enter 3-nd number: '))
# res = True if a < b < c else False
# print(res)
#
# print (a < b < c)

# 2
# Большее число
# Напишите программу, которая получит два числа от пользователя и выведет большее из них. Если числа
# равны, программа должна вывести "Числа равны"
# a, b, = int(input('Enter 1-st number: ')),\
#         int(input('Enter 2-nd number: '))
# if a > b:
#     print('Большее число:', a)
# elif b > a:
#     print('Большее число:', b)
# else:
#     print('Числа равны.')

# Определение четности числа
# Напишите программу, которая получит число от пользователя и выведет, что это число: "Четное" или
# "Нечетное". Решите обычным и тернарным оператором.
# number = int(input("Enter a number: "))
# if number % 2:
#     print("Число не четное.")
# else:
#     print("Число четное.")

# a = int(input("Enter a number: "))
# res = "Число не четное." if a % 2 else 'Число четное.'
# print(res)

# Задание 2
# Категории возраста
# Напишите программу, которая получит от пользователя возраст и выведет соответствующую категорию:
# ребенок (меньше 12 лет), подросток (от 12 до 18, взрослый (от 18 до 60, пожилой (больше 60.

# age = int(input("Введите возраст: "))
# if age == 0:
#     print('Нерожденный')
# elif age < 12:
#     print('Ребенок')
# elif age < 18:
#     print('Подросток')
# elif age < 60:
#     print('Взрослый')
# else:
#     print('Пожилой')



# 5
# Существование треугольника
# Напишите программу, которая получит три числа от пользователя и определит, может ли существовать
# треугольник с такими сторонами. Условие существования треугольника: сумма любых двух сторон должна
# быть больше третьей.

# a, b, c = int(input('Enter 1-st number: ')),\
#                    int(input('Enter 2-nd number: ')), \
#                    int(input('Enter 3-nd number: '))
# if a + b > c and a + c > b and b + c > a:
#     print('Такой треугольник может существовать.')
# else:
#     print('Такой треугольник не может существовать.')

# Пустая строка
# Напишите программу, которая принимает строку и проверяет, является ли она пустой.

# a = input('Введите строку: ')
#
# if a:
#     print('Строка не пуста')
# else:
#     print('Строка пустая')


# Определение квадранта
# Напишите программу, которая запрашивает координаты
# точки по осям x и y и определяет, в каком квадранте она
# находится, либо то что она находится на одной из осей.

# x = int(input('Введите координату x: '))
# y = int(input('Введите координату y: '))
#
# if x > 0 and y > 0:
#     print('Точка находится в первом квадранте.')
# elif x < 0 and y > 0:
#     print('Точка находится во второй квадранте: ')
# elif x < 0 and y < 0:
#     print('Точка находится в третьем квадранте: ')
# else:
#     print('Точка находится в четвертом квадранте: ')

# Допустимые значение времени
# Напишите программу, которая запрашивает у пользователя часы и минуты и проверяет, являются ли они
# допустимыми значениями времени.

# hour, minutes = int(input('Введите часы: ' )),\
#                 int(input('Введите минуты: ' ))
# if 0 <= hour <= 24 and 0 <= minutes <= 60:
#     print('Введенное время:', hour, 'часов', minutes, 'минут')
# else:
#     print('Время введено не корректно')


# Знак произведения
# Напишите программу, которая принимает три числа и определяет знак их произведения без явного
# умножения.

# a, b, c = int(input('Enter 1-st number: ')),\
#           int(input('Enter 2-nd number: ')), \
#           int(input('Enter 3-nd number: '))
# if a > 0 and b > 0 and c > 0:
#     print('Произведение чисел положительное.')
# elif (a < 0 and b < 0) or (c < 0 and b < 0):
#     print('Произведение чисел положительное.')
# else:
#     print('Произведение чисел отрицательное.')

# salary = int(input('Введите доход: '))
# if salary <= 10000:
#     print('Налог 5% составляет:', salary * 0.05, '\nИтоговая сумма после уплаты налога:', salary - (salary * 0.05))
# elif 50000 >= salary >= 10001:
#     print('Налог 10% составляет:', salary * 0.1, '\nИтоговая сумма после уплаты налога:', salary - (salary * 0.1))
# elif salary > 50000:
#     print('Налог 20% составляет:', salary * 0.2, '\nИтоговая сумма после уплаты налога:', salary - (salary * 0.2))

# temp, wind, rain   = int(input('Введите температуру: ')),\
#                     int(input('Введите скорость ветра: ')),\
#                     int(input('Введите уровень осадков (в мм): '))
# if  temp <= -10 and wind > 20:
#     print('Предупреждение: экстремальная погода! Оставайтесь дома!')
# elif temp > 35:
#     print('Предупреждение: экстремальная погода! Оставайтесь дома!')
# elif rain > 50:
#     print('Предупреждение: экстремальная погода! Оставайтесь дома!')
# else:
#     # Ни одно условие не выполнено → погода нормальная
#     print("Погода в пределах нормы. Хорошего дня.")

temp, wind, rain   = int(input('Введите температуру: ')),\
                    int(input('Введите скорость ветра: ')),\
                    int(input('Введите уровень осадков (в мм): '))

print("⚠️ Предупреждение: экстремальная погода! Оставайтесь дома!"
    if (temp < -10 and wind > 20) or temp > 35 or rain > 50
    else "Погода в пределах нормы.")









