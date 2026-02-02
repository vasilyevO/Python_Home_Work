# Тестирование объекта на truth

# x = 0
# print(bool(x))
# x = 100
# print(bool(x))
# x = -100
# print(bool(x))
#
# # Numbers as False - 0, 0.0, 0j, False
# # Seq as False - пустая последовательность, т.е. в которой нет ни одного элемента, '', [], (), {}, set()
# # None - False
# print(23e-2)
# print(0.23e2)


# name = input("Enter your name: ")
# Bad style
# if len(name) > 0:
#     print(name.upper())
# else:
#     print("Name cannot be empty")

#
# if name:
#     print(name.upper())
# else:
#     print("Name cannot be empty")
#
#
# if "":
#     print("NO")
# else:
#     print("YES")
#

# a = int(input('Enter a number: '))
#
# if not a % 2:
#     print(a ** 3)

#
# name = input("Enter your name: ")
# if not name:
#     print("Please enter your name")

#
# salary = int(input('Enter your salary: '))
# res_1 = salary >= 2000 and salary <= 5000 # bad style
#
# res_1 = 2000 <= salary <= 5000
#
# print('In 2000-5000:', res_1 )
#
# res_2 = salary < 2000 or salary > 5000
# print('Not In 2000-5000:', res_2 )
# print('Not In 2000-5000:', not res_1)

# salary = int(input('Enter your salary: '))
# # res_1 = salary >= 2000 and salary <= 5000 # bad style
#
# res_1 = 2000 <= salary <= 5000
#
# print('In 2000-5000:', res_1 )
#
# res_2 = salary < 2000 or salary > 5000
# print('Not In 2000-5000:', res_2 )
# print('Not In 2000-5000:', not res_1)

# a = 5
# b = 10
# print(a < b and b < 10)

# ДЗ 4
# Задание 1
first_value = input("Enter first value (True/False): ")
second_value = input("Enter second value (True/False): ")
first_bool = bool(first_value == 'True')
second_bool = bool(second_value == 'True')
print("and:", first_bool and second_bool)
print("or:", first_bool or second_bool)
print("not:", not first_bool)
print("equal:", first_bool == second_bool)
print("not equal:", first_bool != second_bool)

# Задание 2
# window_open, light_on = int(input('Напишите цифрой открыто ли окно? 1 - Да, 0 - Нет: ')),\
#                         int(input('Напишите, цифрой включен ли свет? 1 - Да, 0 - Нет: '))
# res_1 = window_open == 1
# print('Окно открыто?:', res_1)
# res_2 = light_on == 1
# print('Свет включен?:', res_2)
# print('Оба условия выполнены?:', res_1 and res_2)
# print('Хотя бы одно условие выполнено?:', res_1 or res_2)

# Задание 3
traffic = int(input("Введите количество использованных вами МБ: "))
basic_tariff = 30
add_pay = (traffic - 500) * (traffic > 500) * 0.2
# total_cost = price * quantity
# change = payment - total_cost
print("Ваш базовый тариф: 30 евро за 500 МБ")
print("Общая стоимость:", basic_tariff + add_pay, "евро.", "\nИз них переплата: ", add_pay, "евро.")

# res = basic_tariff + max(traffic - 500,0)
# print(res)




# a = 0
# b = 6
#
# res = a or b
# print(res, bool(res))







