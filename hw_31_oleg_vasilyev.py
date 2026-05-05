print("\n 1. Извлечение дат")

import re
def extract_dates(text: str) -> list[str]:
    """
    Finds all dates in the text in the following formats DD/MM/YYYY, DD.MM.YYYY, DD-MM-YYYY.

    Args:
        text: source text for date search.

    Returns:
        List of dates found in their original format.
    """
    pattern = r"\d{2}[/\-.]\d{2}[/\-.]\d{4}"
    return re.findall(pattern, text)

text = "The events N 123456 happened on 15/03/2025, 01.12.2024 and 09-09-2023. Deadline: 28/02/2022."

dates = extract_dates(text)
for date in dates:
    print(date)

print("\n 2. Разделение списка тегов")
import re
def parse_tags(tag_input: str) -> list[str]:
    """
    Splits a line of tags into individual tags.
    Separators can include commas, semicolons, slashes and spaces.

    Args:
        tag_input: a line containing tags separated by any delimiters.

    Returns:
        A list of tags with no empty values.
    """
    tags = re.split(r"[,;/\s]+", tag_input)
    return [tag for tag in tags if tag]


tag_input = "python, data-science / machine-learning; AI neural-networks"
tags = parse_tags(tag_input)
print(tags)