# Задание 1

for task in range(1, 4):
    match task:
        case 1:
            print("1.Таблица умножения")
            number =  int(input("Введите число: "))
            for i in range(1, number + 1):
                for j in range(1, number + 1):
                    print(i * j, end="\t")
                print()

# Задание 2
print("2.Лестница чисел")
number = int(input("Введите число: "))
for row in range(1, number + 1):
    for line in range(1, row + 1):
        print(line, end=" ")
    print()

# Задание 3
print("3.Удаление всех повторяющихся символов")
string = input("Введите строку: ")
            result = ""
            for char in string:
                if char not in result:
                    result += char
            print("Результат: ", result)