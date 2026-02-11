print("1 Задание.Торговый автомат")
price = int(input("Введите стоимость товара: "))
weight = [50, 10, 5, 2, 1]
for coin in weight:
    int_part = price // coin
    if int_part:
        print(f"Внесите монеты номиналом {coin}:", int_part)
        price %= coin

print("2 Задание.Квадрат нечетных чисел")
numbers = list(map(int, input("Введите числа через запятую: ").split(",")))
result = [n ** 2 for n in numbers if n % 2 == 0]
print("Изначальный список:", numbers)
print("Измененный список:", result)
