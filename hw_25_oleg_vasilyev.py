
print("\n 1. Деление без ошибок")


def safe_divide(numerator_raw: str, denominator_raw: str) -> float:
    """
    Performs division of two numbers provided as strings.

    Args:
        numerator_raw (str): The number to be divided.
        denominator_raw (str): The number to divide by.

    Returns:
        float: The result of the division.

    Raises:
        ValueError: If the input strings cannot be converted to float.
        ZeroDivisionError: If the denominator is zero.
    """
    try:
        num = float(numerator_raw)
        den = float(denominator_raw)
        return num / den

    except (ValueError, ZeroDivisionError) as e:
        raise e

try:
    val1 = input("Введите делимое: ")
    val2 = input("Введите делитель: ")

    res = safe_divide(val1, val2)
    print(f"Результат деления: {res}")

except ValueError:
    print("Ошибка: Вы ввели не число!")
except ZeroDivisionError:
    print("Ошибка: Нельзя делить на ноль!")


print("\n 2. Логирование ошибок")
import logging

logging.basicConfig(
    filename="errors.log",
    format='%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s',
    level=logging.ERROR,
    encoding='utf-8'
)


def safe_divide(numerator_raw: str, denominator_raw: str) -> float:
    """
    Performs division and logs errors to 'errors.log' before raising them.

    Args:
        numerator_raw (str): The number to be divided.
        denominator_raw (str): The number to divide by.

    Returns:
        float: Result of the division.

    Raises:
        ValueError: If input is not a number.
        ZeroDivisionError: If division by zero is attempted.
    """
    try:
        num = float(numerator_raw)
        den = float(denominator_raw)
        return num / den

    except (ValueError, ZeroDivisionError) as e:
        logging.error(f"Division error: {e}")
        raise e

try:
    val1 = input("Введите делимое: ")
    val2 = input("Введите делитель: ")

    res = safe_divide(val1, val2)
    print(f"Результат: {res}")

except Exception:
    print("Произошла ошибка. Подробности записаны в errors.log")

