print("\n 1. Анализ курсов студентов")

import json
from datetime import datetime
from collections import Counter
from itertools import chain

def load_data(filename: str) -> list[dict]:
    """Reads a JSON file and returns a list of students."""
    with open(filename, "r", encoding="utf-8") as f:  # отступ 4 пробела
        return json.load(f)                            # отступ 8 пробелов

def calculate_age(birth_date: str, enrollment_date: str) -> float:
    """Calculates the student's age at the time of enrolment."""
    birth = datetime.strptime(birth_date, "%d.%m.%Y")
    enrollment = datetime.strptime(enrollment_date, "%d.%m.%Y")
    return (enrollment - birth).days / 365.25

def analyze(data: list[dict]) -> dict:
    """Calculates statistics on students."""
    total_students = len(data)
    ages = [calculate_age(s["birth_date"], s["enrollment_date"]) for s in data]
    average_age = sum(ages) / len(ages)
    all_courses = chain.from_iterable(s["courses"] for s in data)
    students_per_course = dict(Counter(all_courses))
    return {
        "total_students": total_students,
        "average_enrollment_age": round(average_age, 1),
        "students_per_course": students_per_course
    }

def save_report(report: dict, filename: str) -> None:
    """Saves the report to a JSON file."""
    with open(filename, "w", encoding="utf-8") as f:  # filename, не хардкод!
        json.dump(report, f, indent=4)                 # dump, не dumps!

data = load_data("student_courses.json")
report = analyze(data)
save_report(report, "student_courses.json")
print(json.dumps(report, indent=4))