"""Day 1 Practice: Python vs Java Execution Comparison & Type Hints Demo.

This script demonstrates Python's dynamic typing, execution flow,
and modern type hint practices compared to static compilation concepts.
"""



def calculate_total_salary(base: int, bonus: int) -> int:
    """Calculates total compensation using explicit type hints.

    Args:
        base: Base salary amount.
        bonus: Additional bonus amount.

    Returns:
        Total calculated salary as an integer.

    """
    return base + bonus


if __name__ == "__main__":
    # Python execution demonstration
    base_pay: int = 50000
    performance_bonus: int = 5000

    total: int = calculate_total_salary(base_pay, performance_bonus)
    print(f"Total Calculated Salary: {total}")
