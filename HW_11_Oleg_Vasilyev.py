

print("Задание 1. Звёздочки вместо чисел.")
text = "My number is 123-456-789"
for char in text:
    if char.isdigit():
        text = text.replace(char, str("*"))
print(text)

print("Задание 2. Количество символов.")
text = "Programming in python"
print("Строка:", text)
for char in text.casefold():
    print(f"Символ '{char}' встречается {text.count(char)} раз(а)") if text.count(char) > 1 else None
    text = text.replace(char, "")

Вариант 2:
print("Задание 2. Количество символов.")

text = "Programming in python".casefold()
printed = ""
print("Строка:", text)

for char in text:
    if char in printed:
        continue
    count = text.count(char)
    if count > 1:
        print(f"Символ '{char}' встречается {count} раз(а)")
        printed += char


# Увеличение чисел
# Напишите программу, которая заменяет все числа в строке на их эквивалент, умноженный на 10.
# text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
# Пример вывода:
# I have 50.0 apples and 100.0 oranges, price is 5.0 each. Card number is ....3672.

text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
new_symbols = []
for char in text.split():
    if char.count('.') <= 1 and char.replace('.', '').isdigit():
         char = str(float(char) * 10)
    new_symbols.append(char)
new_text = " ".join(new_symbols)
print(new_text)
