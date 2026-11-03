"""Print a greeting using an optional environment variable."""

import os


if __name__ == "__main__":
    name = os.getenv("WHO_TO_GREET", "GitHub Actions Student")
    print(f"Hello {name}!")
    print("This program is running inside GitHub Actions.")
