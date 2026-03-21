print("\n 1. Простое число.")

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Введите число для проверки: "))
if is_prime(n):
    print(f"Число {n} является простым")
else:
    print(f"Число {n} не является простым")


print("\n 2. Фильтрация чисел по чётности.")

def filter_numbers(filter_type, *args):
    if filter_type == "even":
        return [num for num in args if num % 2 == 0]
    elif filter_type == "odd":
        return [num for num in args if num % 2 == 1]
    else:
        return "Вы ввели некорректный фильтр."

print(filter_numbers("even", 1, 2, 3, 4, 5, 6))
print(filter_numbers("odd", 10, 15, 20, 25))
print(filter_numbers("prime", 2, 3, 5, 7))


print("\n 3. Объединение словарей.")
def merge_dicts(*args):
    result = {}
    for d in args:
        result.update(d)
    return result

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {"d": 5}

print(merge_dicts(dict1, dict2, dict3))