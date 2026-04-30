import csv
from pathlib import Path
from datetime import datetime


DATA_FILE = Path("expenses.csv")
FIELDNAMES = ["date", "category", "description", "amount"]


def ensure_file_exists():
    if not DATA_FILE.exists():
        with DATA_FILE.open("w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()


def add_expense():
    date_text = input("Date (YYYY-MM-DD, blank for today): ").strip()
    if not date_text:
        date_text = datetime.today().strftime("%Y-%m-%d")

    category = input("Category: ").strip().title()
    description = input("Description: ").strip()

    try:
        amount = float(input("Amount: ").strip())
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    with DATA_FILE.open("a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writerow({
            "date": date_text,
            "category": category,
            "description": description,
            "amount": f"{amount:.2f}",
        })

    print("Expense added successfully.")


def read_expenses():
    ensure_file_exists()
    with DATA_FILE.open("r", newline="") as file:
        return list(csv.DictReader(file))


def view_expenses():
    expenses = read_expenses()
    if not expenses:
        print("No expenses found.")
        return

    print("\nDate        Category        Amount     Description")
    print("-" * 60)
    for expense in expenses:
        print(
            f"{expense['date']:<11} "
            f"{expense['category']:<15} "
            f"{expense['amount']:<10} "
            f"{expense['description']}"
        )


def show_summary():
    expenses = read_expenses()
    if not expenses:
        print("No expenses found.")
        return

    total = 0
    category_totals = {}

    for expense in expenses:
        amount = float(expense["amount"])
        category = expense["category"]
        total += amount
        category_totals[category] = category_totals.get(category, 0) + amount

    print(f"\nTotal spending: {total:.2f}")
    print("\nCategory summary")
    print("-" * 30)
    for category, amount in sorted(category_totals.items()):
        print(f"{category:<15} {amount:.2f}")


def main():
    ensure_file_exists()

    while True:
        print("\nExpense Tracker")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Show summary")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_summary()
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()

