
print("\n 1. Список всех стран")

import os
import pymysql
from dotenv import load_dotenv


load_dotenv('.env')

config = {'host': os.getenv('DB_HOST'),
          'user': os.getenv('DB_USER'),
          'password': os.getenv('DB_PASSWORD'),
          'database': os.getenv('DB_NAME'),
          }
class Country:
    COUNTRY_QUERY = """
                        SELECT name
                        FROM country 
                        """

    def __init__(self, cur):
        self.cur = cur

    def get_country(self):
        self.cur.execute(self.COUNTRY_QUERY)
        return [row[0] for row in self.cur]

# UI

def print_country(countries):
    for index, country in enumerate(countries, start=1):
        print(index, country)

def main():
    with pymysql.connect(**config) as conn:
        with conn.cursor() as cur:
            country = Country(cur)
            countries = country.get_country()
            print_country(countries)

if __name__ == '__main__':
    main()



print("\n 2. Города выбранной страны")

import os
import pymysql
from dotenv import load_dotenv
from collections import namedtuple

load_dotenv('.env')

config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME'),
}

CurrentCity = namedtuple('CurrentCity', ['CountryName', 'CityName', 'Population'])


class Country:
    """A class for working with countries and cities from the database."""

    COUNTRY_QUERY = """
        SELECT name
        FROM country
    """

    CITIES_QUERY = """
        SELECT con.name, c.name, c.population
        FROM country AS con
        JOIN city AS c ON c.CountryCode = con.Code
        WHERE con.name = %s {country_filter}
        ORDER BY Population DESC
    """

    def __init__(self, cur) -> None:
        """
        Args:
            cur: database connection cursor.
        """
        self.cur = cur

    def get_country(self) -> list[str]:
        """
        Returns a list of all countries from the database.

        Returns:
            List of country names.
        """
        self.cur.execute(self.COUNTRY_QUERY)
        return [row[0] for row in self.cur]

    def get_city(self, city: str, city_filter: str = '') -> list[CurrentCity]:
        """
        Returns a list of cities in the selected country, along with their populations.

        Args:
            city: the name of the country.
            city_filter: an additional SQL filter.

        Returns:
            A namedtuple named `CurrentCity` containing the fields `CountryName`, `CityName` and `Population`.
        """
        self.cur.execute(
            self.CITIES_QUERY.format(country_filter=city_filter),
            (city,)
        )
        return [CurrentCity(*row) for row in self.cur]


def format_countries(countries: list[str]) -> str:
    """
    Formats a list of countries into a numbered string.

    Args:
        countries: a list of country names.

    Returns:
        A numbered list of countries as a string.
    """
    return "\n".join(
        f"{index}. {country}"
        for index, country in enumerate(countries, start=1)
    )

def format_cities(cities: list[CurrentCity]) -> str:
    """
    Formats a list of cities into a numbered string.

    Args:
        cities: a namedtuple list of CurrentCity objects.

    Returns:
        A numbered list of cities, with the population displayed as a string.
    """
    return "\n".join(
        f"{index}. {city.CityName} — {city.Population}"
        for index, city in enumerate(cities, start=1)
    )

def get_selected_country(user_input: str, countries: list[str]) -> str:
    """
    Determines the selected country based on the user’s input.

    Args:
        user_input: user input — a country code or name.
        countries: a list of all countries.

    Returns:
        The name of the selected country.
    """
    if user_input.isdigit():
        return countries[int(user_input) - 1]
    return user_input

def main() -> None:
    """Entry point — connects to the database and executes the main logic."""
    with pymysql.connect(**config) as conn:
        with conn.cursor() as cur:
            country = Country(cur)

            countries = country.get_country()
            print(format_countries(countries))

            user_input = input("Введите страну: ")
            selected_country = get_selected_country(user_input, countries)

            cities = country.get_city(selected_country)
            print(format_cities(cities))

if __name__ == '__main__':
    main()

