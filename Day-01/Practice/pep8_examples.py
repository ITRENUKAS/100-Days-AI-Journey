"""Day 1 Practice: PEP 8 Styling & Code Clean-up Standards.

This module demonstrates proper PEP 8 conventions, spacing, line lengths,
and naming rules for clean, readable Python code.
"""

# Constants use UPPER_CASE
MAX_RETRIES: int = 3
DEFAULT_TIMEOUT: int = 30


class UserAccount:
    """Represents a user account adhering to PascalCase naming rules."""

    def __init__(self, username: str, active: bool = True) -> None:
        """Initializes the user account."""
        self.username = username
        self.active = active

    def get_status(self) -> str:
        """Returns the user status message using f-strings."""
        return f"User {self.username} is active: {self.active}"


def calculate_tax(income: int, tax_rate: float) -> float:
    """Calculates tax using snake_case naming and proper operator spacing."""
    # Correct binary operator spacing (a = b + c style)
    base_tax = income * tax_rate
    return base_tax


if __name__ == "__main__":
    # Demonstration of proper list indexing and function brackets (no space inside brackets)
    sample_list = [10, 20, 30, 40]
    first_element = sample_list[0]
    sliced_list = sample_list[1:3]

    account = UserAccount(username="Renuka")
    print(account.get_status())
    print(f"Calculated Tax: {calculate_tax(50000, 0.15)}")
