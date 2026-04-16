# import os
# import sys
# import logging
#
# logging.basicConfig(
#     filename="errors.log",
#     format='%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s',
#     level=logging.ERROR,
#     encoding='utf-8'
# )
# print("\n 1. Список файлов и папок")
# def main() -> None:
#     """
#     Takes a path as a command-line argument and displays a list
#     of the folders and files it contains.
#     """
#
#     if len(sys.argv) < 2:
#         print("Использование: python script.py <путь_к_директории>")
#         return
#
#     path: str = sys.argv[1]
#     dir_list: list[str] = []
#     file_list: list[str] = []
#
#     try:
#         for name in os.listdir(path):
#             full_path = os.path.join(path, name)
#             if os.path.isdir(full_path):
#                 dir_list.append(name)
#             elif os.path.isfile(full_path):
#                 file_list.append(name)
#
#         print(f"\n Содержимое директории '{path}':")
#
#         if dir_list:
#             print("\nПапки:")
#             for folder in dir_list:
#                 print(f"- {folder}")
#
#         if file_list:
#             print("\nФайлы:")
#             for file in file_list:
#                 print(f"- {file}")
#
#     except FileNotFoundError:
#         logging.error(f"Путь не найден: {path}")
#         print(f"Ошибка: Директория '{path}' не найдена.")
#     except PermissionError:
#         logging.error(f"Нет прав доступа: {path}")
#         print(f"Ошибка: Нет прав доступа к '{path}'.")
#     except Exception as e:
#         logging.error(f"Непредвиденная ошибка: {e}", exc_info=True)
#         print(f"Произошла ошибка. Подробности в 'errors.log'.")
#
# main()

print("\n 2. Поиск и удаление файлов с указанным расширением")

import os
import sys
import logging
from typing import List


def setup_logging() -> None:
    """
    Configures the logging settings for the script.

    The logs are saved to 'cleanup.log' with timestamps and error levels.
    """
    logging.basicConfig(
        filename="cleanup.log",
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        encoding='utf-8'
    )


def find_files(path: str, extension: str) -> List[str]:
    """
    Recursively finds files with a specific extension in a given directory.

    Args:
        path (str): The root directory to start the search.
        extension (str): The file extension to look for (e.g., '.log').

    Returns:
        List[str]: A list of full paths to the found files.

    Raises:
        FileNotFoundError: If no matching files are found in the directory.
    """
    found_files: List[str] = []

    for root, _, files in os.walk(path):
        for filename in files:
            if filename.endswith(extension):
                full_path = os.path.join(root, filename)
                found_files.append(full_path)

    if not found_files:
        # Using a standard built-in exception
        raise FileNotFoundError(f"Не найдено файлов '{extension}' в '{path}'.")

    return found_files


def main() -> None:
    """
    Main entry point of the script.
    Handles arguments, searching, and safe deletion of files.
    """
    setup_logging()

    if len(sys.argv) < 3:
        print("Использование: python script.py <path> <extension>")
        return

    target_path: str = sys.argv[1]
    ext: str = sys.argv[2]

    if not ext.startswith('.'):
        ext = f".{ext}"

    try:
        if not os.path.isdir(target_path):
            print(f"Ошибка: '{target_path}' это несуществующая папка.")
            return

        files_to_delete = find_files(target_path, ext)

        print(f"Найдено {len(files_to_delete)} файлов для удаления:")
        for f in files_to_delete:
            print(f" - {f}")

        confirm = input("\nВы хотите удалить эти файлы? (y/n): ").strip().lower()

        if confirm == 'y':
            deleted_count = 0
            for f in files_to_delete:
                try:
                    os.remove(f)
                    deleted_count += 1
                except OSError as e:
                    logging.error(f"Ошибка удаления {f}: {e}")
                    print(f"Ошибка удаления {f}")

            print(f"\nУспешно удалено {deleted_count} файлов.")
            logging.info(f"Удалено {deleted_count} файлов в {target_path}")
        else:
            print("Операция отменена пользователем.")

    except FileNotFoundError as e:
        print(f"Notice: {e}")
    except Exception as e:
        logging.critical(f"Не предвиденная ошибка: {e}")
        print(f"Возникла неожиданная ошибка. Проверь cleanup.log для подробностей")

main()