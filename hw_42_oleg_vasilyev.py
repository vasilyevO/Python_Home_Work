from multiprocessing import connection

print("\n 1. Создание базы")

import pymysql
import os
from dotenv import load_dotenv


load_dotenv('.env_edit')

config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD')
}

db_name = "notes_app_121225_ptm_oleg_vasyliev"

class Notes:
    """Класс для работы с таблицей заметок."""

    CREATE_TABLE_QUERY = """
            CREATE TABLE IF NOT EXISTS notes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(100),
            content TEXT
        )
    """

    def __init__(self, cur) -> None:
        """
        Args:
            cur: курсор подключения к базе данных.
        """
        self.cur = cur

    def create_table(self) -> None:
        """Создаёт таблицу notes если она не существует."""
        self.cur.execute(self.CREATE_TABLE_QUERY)

def main() -> None:
    """Создаёт базу данных и таблицу заметок."""
    with pymysql.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
            cur.execute(f"USE {db_name}")

            notes = Notes(cur)
            notes.create_table()

            cur.execute("SHOW DATABASES")
            databases = [row[0] for row in cur]

            if db_name in databases:
                print(f"Database '{db_name}' created or already exists.")
            else:
                print("Something went wrong. Database not found.")

if __name__ == '__main__':
    main()

print("\n 2. Добавление заметок")

import pymysql
import os
from dotenv import load_dotenv
from pymysql.cursors import DictCursor

load_dotenv('.env_edit')

config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD')
}

db_name = "notes_app_121225_ptm_oleg_vasyliev"

class Notes:
    """Класс для работы с таблицей заметок."""

    CREATE_TABLE_QUERY = """
        CREATE TABLE IF NOT EXISTS notes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(100),
            content TEXT
        )
    """

    INSERT_QUERY = "INSERT INTO notes (title, content) VALUES (%s, %s)"
    SELECT_QUERY = "SELECT * FROM notes"

    def __init__(self, cur) -> None:
        """
        Args:
            cur: курсор подключения к базе данных.
        """
        self.cur = cur

    def create_table(self) -> None:
        """Создаёт таблицу notes если она не существует."""
        self.cur.execute(self.CREATE_TABLE_QUERY)

    def add_note(self, title: str, content: str) -> None:
        self.cur.execute(self.INSERT_QUERY, (title, content))

    def get_notes(self) -> list[dict]:
        self.cur.execute(self.SELECT_QUERY)
        return self.cur.fetchall()

def main() -> None:
    """Создаёт базу данных и таблицу заметок."""
    try:
        with pymysql.connect(**config, cursorclass=DictCursor) as conn:
            # Обычный cursor для создания БД и таблицы
            with conn.cursor() as cur:
                notes = Notes(cur)
                cur.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
                cur.execute(f"USE {db_name}")
                notes.create_table()

                notes.add_note("Shopping list", "Buy milk, eggs, bread")
                conn.commit()
                print(f"Database '{db_name}' created or already exists.")

            # DictCursor только для SELECT
            with conn.cursor(DictCursor) as dict_cur:
                dict_cur.execute(f"USE {db_name}")
                notes_dict = Notes(dict_cur)
                result = notes_dict.get_notes()
                print("\n".join(
            f"Note added: {note['title']}"
            for note in result))

    except pymysql.MySQLError as e:
        print(f'Database error: {e}')

if __name__ == '__main__':
    main()