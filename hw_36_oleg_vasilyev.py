print("\n 1. Класс Person")

class Person:
    """Класс представляющий человека."""

    def __init__(self, name: str) -> None:
        """
        Инициализирует человека с именем.

        Args:
            name: имя человека.
        """
        self.name = name

    def introduce(self) -> str:
        """Возвращает приветствие с именем."""
        return f"Hallo, my name is {self.name}."

person = Person("Alice")
print(person.introduce())



print("\n 2. Класс Student")

class Person:
    """A class representing a person."""

    def __init__(self, name: str) -> None:
        """
        Initialises a person with a name.

        Args:
            name: a person's name.
        """
        self.name = name

    def introduce(self) -> str:
        """Returns a greeting with a name."""
        return f"Hallo, my name is {self.name}."

class Student(Person):
    """A class representing a student, which inherits from Person."""

    def __init__(self, name: str, course: int) -> None:
        """
        Initialises a student with a name and course number.

        Args:
            name: student's name.
            course: course number.
        """
        super().__init__(name)
        self.course = course

    def introduce(self) -> str:
        """Returns a greeting containing the name and course number."""
        parent_intro = super().introduce()
        return f"{parent_intro}\nI'm on course {self.course}."

student = Student("Alice", 2)
print(student.introduce())



print("\n 3. Класс Teacher и список людей")

class Person:
    """A class representing a person."""

    def __init__(self, name: str) -> None:
        """
        Initialises a person with a name.

        Args:
            name: a person's name.
        """
        self.name = name

    def introduce(self) -> str:
        """Returns a greeting with a name."""
        return f"Hallo, my name is {self.name}."

class Student(Person):
    """A class representing a student, which inherits from Person."""

    def __init__(self, name: str, course: int) -> None:
        """
        Initialises a student with a name and course number.

        Args:
            name: student's name.
            course: course number.
        """
        super().__init__(name)
        self.course = course

    def introduce(self) -> str:
        """Returns a greeting containing the name and course number."""
        parent_intro = super().introduce()
        return f"{parent_intro}\nI'm on course {self.course}."

class Teacher(Person):
    def __init__(self, name: str, subject: str) -> None:
        super().__init__(name)
        self.subject = subject

    def introduce(self) -> str:
        return f"Hello, I am professor {self.name}.\nMy subject is {self.subject}."

people = [Student("Alice", 2), Teacher("Bob", "Mathematics")]

for person in people:
    print(person.introduce())
