print("\n 1. Электронное письмо")

from datetime import datetime

class Email:
    """A class representing an email."""

    def __init__(self, sender: str, recipient: str,
                 subject: str, body: str, date: datetime) -> None:
        """
        Args:
            sender: адрес отправителя.
            recipient: адрес получателя.
            subject: тема письма.
            body: текст письма.
            date: дата отправки.
        """
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body
        self.date = date

    def __str__(self) -> str:
        """Returns a string representation of the letter."""
        return (f"From: {self.sender}\n"
                f"To: {self.recipient}\n"
                f"Subject: {self.subject}\n"
                f"- {self.body} -")

    def __len__(self) -> int:
        """Returns the length of the text of the letter."""
        return len(self.body)

    def __bool__(self) -> bool:
        """Returns True if the email contains non-empty text."""
        return bool(self.body.strip())

    def __gt__(self, other: "Email") -> bool:
        """Sorts emails by date sent."""
        return self.date > other.date


e1 = Email("alice@example.com", "bob@example.com",
           "Meeting", "Let's meet at 10am", datetime(2024, 6, 10))
e2 = Email("bob@example.com", "alice@example.com",
           "Report", "", datetime(2024, 6, 11))

print(e1)
print(e2)
print("Length:", len(e1))
print("Has text:", bool(e1))
print("Is newer:", e2 > e1)


print("\n 2. Класс для работы с деньгами")

class Money:
    """A class for working with monetary amounts."""

    def __init__(self, amount: float) -> None:
        """
        Args:
            amount: sum of money.
        """
        self.amount = amount

    def __str__(self) -> str:
        """Returns a string in the format $amount."""
        return f"${self.amount}"

    def __add__(self, other: "Money") -> "Money":
        """Returns a new object containing the sum of the two objects."""
        return Money(self.amount + other.amount)

    def __sub__(self, other: "Money") -> "Money":
        """Returns a new object containing the difference. Minimum 0."""
        result = max(0, self.amount - other.amount)
        return Money(result)

money1 = Money(100)
money2 = Money(50)
print(money1 + money2)
print(money1 - money2)
print(money2 - money1)