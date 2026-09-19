"""Day 1 Practice: Code Clean-up, Docstrings, & Refactoring Demo.

This script demonstrates modern Python clean-up practices, including docstring
metadata inspection and f-string interpolation instead of legacy concatenation.
"""


def format_user_greeting(username: str, role: str | None = None) -> str:
    """Generates a professional greeting using modern f-strings.

    Args:
        username: The name of the user.
        role: Optional job title or role.

    Returns:
        A formatted greeting string.
    """
    # Modern f-string refactoring (Avoids legacy string concatenation like "+" or "%")
    user_role = role if role else "Professional Fresher"
    return f"Welcome back, {username}! Role: {user_role}."


if __name__ == "__main__":
    # 1. Test the refactored f-string greeting function
    greeting_message = format_user_greeting(username="Renuka", role="AI Developer")
    print(greeting_message)

    # 2. Inspect the docstring metadata dynamically (Python Inspection Feature)
    print("\n=== Docstring Inspection Demo ===")
    print(format_user_greeting.__doc__)
