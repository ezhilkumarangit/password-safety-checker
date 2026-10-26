"""
Password Safety Checker
A tiny beginner-friendly cybersecurity project.
Uses only Python's standard library.
"""

import secrets
import string

COMMON_PASSWORDS = {
    "password", "password123", "123456", "12345678",
    "qwerty", "admin", "letmein", "welcome"
}


def check_password(password):
    """Return a simple strength rating and the reasons behind it."""
    checks = {
        "At least 12 characters": len(password) >= 12,
        "Contains lowercase letters": any(c.islower() for c in password),
        "Contains uppercase letters": any(c.isupper() for c in password),
        "Contains a number": any(c.isdigit() for c in password),
        "Contains a symbol": any(not c.isalnum() for c in password),
    }

    score = sum(checks.values())
    if password.lower() in COMMON_PASSWORDS:
        rating = "Very weak"
    elif score <= 2:
        rating = "Weak"
    elif score <= 4:
        rating = "Moderate"
    else:
        rating = "Strong"

    return rating, checks


def generate_password(length=16):
    """Generate a random password using Python's secure secrets module."""
    if length < 12:
        raise ValueError("Choose a length of at least 12 characters.")

    alphabet = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(alphabet) for _ in range(length))


def main():
    print("=== Password Safety Checker ===")
    print("1. Check a password")
    print("2. Generate a strong password")
    choice = input("Choose 1 or 2: ").strip()

    if choice == "1":
        password = input("Enter a password to check: ")
        rating, checks = check_password(password)
        print("\nRating:", rating)
        for description, passed in checks.items():
            print(("[OK] " if passed else "[NO] ") + description)
        print("\nTip: Use a unique password for every account.")
        print("This is a basic local check, not a guarantee of security.")

    elif choice == "2":
        try:
            length_text = input("Password length (12 or more, default 16): ").strip()
            length = int(length_text) if length_text else 16
            print("\nGenerated password:", generate_password(length))
            print("Save it in a trusted password manager.")
        except ValueError as error:
            print("Error:", error)

    else:
        print("Please choose 1 or 2.")


if __name__ == "__main__":
    main()
