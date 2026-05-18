print("\n 1. Банковский счёт")

class BankAccount:
    """A bank account class with an encapsulated balance."""

    def __init__(self, owner: str, balance: float) -> None:
        """
        Initialises an account with the account holder's name and an opening balance.

        Args:
            owner: account holder's name.
            balance: opening balance.
        """
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount: float) -> None:
        """
        Top up your account by the specified amount.

        Args:
            amount: top-up amount.

        Raises:
            ValueError: if the sum is not positive.
        """
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        """
        Withdraws funds from the account.

        Args:
            amount: withdrawal amount.

        Raises:
            ValueError: if there are insufficient funds.
        """
        if amount > self.__balance:
            raise ValueError("Not enough funds.")
        self.__balance -= amount

    def get_balance(self) -> float:
        """Returns a string containing the current balance."""
        return self.__balance

account = BankAccount("Alice", 150)
print(f"Current balance: {account.get_balance()}")

try:
    account.deposit(-50)
except ValueError as e:
    print(f"Error: {e}")

print(f"Current balance: {account.get_balance()}")

try:
    account.withdraw(500)
except ValueError as e:
    print(f"Error: {e}")

print(f"Current balance: {account.get_balance()}")


print("\n 2. Банковский счёт с историей операций")
class BankAccount:
    """A bank account class with a transaction history."""

    def __init__(self, owner: str, balance: float) -> None:
        """
        Creates an account with the account holder's name and an opening balance.

        Args:
            owner: account holder's name.
            balance: opening balance.
        """
        self.owner = owner
        self.__balance = balance
        self.__history: list[str] = []

    def deposit(self, amount: float) -> None:
        """
        Top up your account by the specified amount.

        Args:
            amount: top-up amount.

        Raises:
            ValueError: if the sum is not positive.
        """
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        self.__balance += amount
        self.__history.append(f"Deposit: {amount}")

    def withdraw(self, amount: float) -> None:
        """
        Withdraws funds from the account.

        Args:
            amount: withdrawal amount.

        Raises:
            ValueError: if there are insufficient funds.
        """
        if amount > self.__balance:
            raise ValueError("Not enough funds.")
        self.__balance -= amount
        self.__history.append(f"Withdraw: {amount}")

    def get_balance(self) -> float:
        """Returns a string containing the current balance."""
        return self.__balance

    @property
    def history(self) -> list[str]:
        """Returns a read-only transaction history."""
        return self.__history

account = BankAccount("Alice", 0)
account.deposit(150)
account.withdraw(100)
print(f"Current balance: {account.get_balance()}")
print("Operation history:")
for record in account.history:
    print(f"    {record}")