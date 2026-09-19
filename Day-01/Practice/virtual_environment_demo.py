"""Day 1 Practice: Virtual Environment & Package Management Demo.

This script demonstrates how to check the active Python environment,
inspect system execution paths, and verify dependency isolation.
"""

import sys


def check_environment_details() -> None:
    """Prints current interpreter path and environment isolation status."""
    print("=== Python Environment Diagnostics ===")
    print(f"Executable Path: {sys.executable}")
    print(f"Python Version: {sys.version.split()[0]}")

    # Check if running inside a virtual environment (venv/poetry/conda)
    is_venv = hasattr(sys, "real_prefix") or (
        hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix
    )
    print(f"Running inside Virtual Environment: {is_venv}")

    if is_venv:
        print("Status: SUCCESS! Your dependencies are cleanly isolated.")
    else:
        print("Warning: Running on global system Python. Consider activating a venv!")


if __name__ == "__main__":
    check_environment_details()
