print("\n 1. Счётчик экземпляров")

class User:
    """A class representing a user. It maintains a count of all users created."""

    total_users: int = 0

    def __init__(self, username: str, password: str) -> None:
        """
        Initialises the user and increments the counter.

        Args:
            username: username.
            password: user password.
        """
        self.username = username
        self.password = password
        User.total_users += 1

    def get_total(self) -> int:
        """Returns the total number of users created."""
        return User.total_users

user1 = User("alice", "pass123")
user2 = User("bob", "pass456")
print(f"Total users: {User.get_total(user1)}")


print("\n 2. Проверка данных пользователя")

class User:
    """"A user class with login and password validation."""
    total_users: int = 0
    MIN_PASSWORD_LENGTH: int = 5

    def __init__(self, username: str, password: str) -> None:

        """
        Initialises the user with data validation.

        Args:
            username: username — a non-empty string.
            password: password — at least 5 characters.

        Raises:
            ValueError: if the username is empty or the password is less than 5 characters long.
        """
        if not username.strip():
            raise ValueError(f"Invalid username: '{username}'.")
        if len(password.strip()) < User.MIN_PASSWORD_LENGTH:
            raise ValueError(f"Invalid password: '{password}'.")

        self.username = username.strip()
        self.password = password.strip()
        User.total_users += 1

    def __str__(self) -> str:
        """Returns the user's string representation."""
        return f"User: {self.username}"


try:
    user1 = User("alice", "secret")
    print(user1)
except ValueError as e:
    print(f"ValueError: {e}")

try:
    user2 = User("bob", "qwe")
    print(user2)
except ValueError as e:
    print(f"ValueError: {e}")

try:
    user3 = User("bill", "     ")
    print(user2)
except ValueError as e:
    print(f"ValueError: {e}")