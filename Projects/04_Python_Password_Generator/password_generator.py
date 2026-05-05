import argparse
import secrets
import string


LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
DIGITS = string.digits
SYMBOLS = "!@#$%^&*()-_=+[]{};:,.?/<>"


def build_character_pool(include_symbols=True):
    pool = LOWERCASE + UPPERCASE + DIGITS
    if include_symbols:
        pool += SYMBOLS
    return pool


def generate_password(length=16, include_symbols=True):
    if length < 8:
        raise ValueError("Password length must be at least 8 characters.")

    pool = build_character_pool(include_symbols)
    password = [
        secrets.choice(LOWERCASE),
        secrets.choice(UPPERCASE),
        secrets.choice(DIGITS),
    ]

    if include_symbols:
        password.append(secrets.choice(SYMBOLS))

    while len(password) < length:
        password.append(secrets.choice(pool))

    secrets.SystemRandom().shuffle(password)
    return "".join(password)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate secure random passwords from the command line."
    )
    parser.add_argument(
        "-l",
        "--length",
        type=int,
        default=16,
        help="Password length. Minimum: 8. Default: 16.",
    )
    parser.add_argument(
        "-c",
        "--count",
        type=int,
        default=1,
        help="Number of passwords to generate. Default: 1.",
    )
    parser.add_argument(
        "--no-symbols",
        action="store_true",
        help="Generate passwords without special characters.",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    if args.count < 1:
        raise ValueError("Count must be at least 1.")

    for _ in range(args.count):
        print(generate_password(args.length, include_symbols=not args.no_symbols))


if __name__ == "__main__":
    main()
