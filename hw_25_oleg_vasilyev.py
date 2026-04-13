
print("\n 1. Деление без ошибок")

def safe_divide() -> None:
    """
    Запрашивает у пользователя два числа и выводит результат деления,
    обрабатывая ошибки ввода и деления на ноль.
    """
    try:
        numerator = float(input("Введите делимое: "))
        denominator = float(input("Введите делитель: "))
        result = numerator / denominator

    except ValueError:
        print("Ошибка: Введено некорректное число.")
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль.")
    else:
        print(f"Результат деления: {result}")

safe_divide()


print("\n 2. Логирование ошибок")
import logging

logging.basicConfig(
    filename="errors.log",
    format='%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s',
    level=logging.ERROR,
    encoding='utf-8'
)

def safe_divide():
    try:
        a = float(input("Введите делимое: "))
        b = float(input("Введите делитель: "))
        result = a / b
        print(f"Результат: {result}")
    except ValueError:
        logging.error("Ошибка: Введено некорректное число.")
    except ZeroDivisionError:
        logging.error("Ошибка: Деление на ноль.")

safe_divide()