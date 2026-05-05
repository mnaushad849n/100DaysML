# Python Password Generator

A small command-line Python project that generates secure random passwords with the standard library.

## Features

- Choose password length
- Generate one or many passwords
- Include or remove symbols
- Ensures every password contains lowercase, uppercase, and digits

## Run

```bash
python password_generator.py
```

Generate three 20-character passwords:

```bash
python password_generator.py --length 20 --count 3
```

Generate a password without symbols:

```bash
python password_generator.py --no-symbols
```

## Requirements

Python 3.10 or newer. No external packages are required.
