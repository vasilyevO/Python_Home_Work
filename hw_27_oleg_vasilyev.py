print("\n 1. Фильтрация по ключевому слову")

import os

filename = input("Введите имя файла: ")

if not os.path.isfile(filename):
    print(f"Ошибка: файл '{filename}' не найден.")
else:
    keyword = input("Введите ключевое слово: ")

    with open(filename, "r", encoding="utf-8") as f:
        matched_lines = [line for line in f if keyword in line]

    new_filename = f"{keyword}_{filename}"

    if matched_lines:
        with open(new_filename, "w", encoding="utf-8") as out:
            out.writelines(matched_lines)
        print(f"Строки, содержащие '{keyword}', сохранены в {new_filename}.")
    else:
        print(f"Совпадений по слову '{keyword}' не найдено. Файл не создан.")

print("\n 2. Поиск и удаление дубликатов")

import os

filename = input("Введите имя файла: ")

if not os.path.isfile(filename):
    print(f"Ошибка: файл '{filename}' не найден.")
else:
    seen = set()
    unique_lines = []

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            if line not in seen:
                unique_lines.append(line)
                seen.add(line)

    new_filename = f"unique_{filename}"

    with open(new_filename, "w", encoding="utf-8") as out:
        out.writelines(unique_lines)

    print(f"Уникальные строки сохранены в {new_filename}.")