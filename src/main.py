
import json
from pathlib import Path
from datetime import date

DATA_FILE = Path(__file__).parent.parent / "transactions.json"


def load_transactions():
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read saved transactions.")
        return []


def save_transactions(transactions):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(transactions, file, indent=4)


def add_transaction(transactions):
    kind = input("Type (income/expense): ").strip().lower()

    if kind not in ("income", "expense"):
        print("Please enter income or expense.")
        return

    description = input("Description: ").strip()
    category = input("Category: ").strip()

    if not description or not category:
        print("Description and category cannot be empty.")
        return

    try:
        amount = round(float(input("Amount (R): ")), 2)
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid amount.")
        return

    transactions.append({
        "type": kind,
        "description": description,
        "category": category,
        "amount": amount,
        "date": date.today().isoformat()
    })

    save_transactions(transactions)
    print("Transaction saved successfully!")


def view_transactions(transactions):
    if not transactions:
        print("No transactions recorded yet.")
        return

    print("\n--- TRANSACTIONS ---")

    for item in transactions:
        print(
            f'{item["date"]} | {item["type"].title()} | '
            f'{item["description"]} | {item["category"]} | '
            f'R{item["amount"]:.2f}'
        )


def show_summary(transactions):
    income = sum(
        item["amount"] for item in transactions
        if item["type"] == "income"
    )

    expenses = sum(
        item["amount"] for item in transactions
        if item["type"] == "expense"
    )

    print("\n--- FINANCIAL SUMMARY ---")
    print(f"Total income:   R{income:.2f}")
    print(f"Total expenses: R{expenses:.2f}")
    print(f"Balance:        R{income - expenses:.2f}")


def show_monthly_summary(transactions):
    month = input("Enter month (YYYY-MM): ").strip()

    try:
        date.fromisoformat(month + "-01")
    except ValueError:
        print("Use YYYY-MM format, for example 2026-10.")
        return

    monthly = [
        item for item in transactions
        if item.get("date", "").startswith(month)
    ]

    print(f"\n--- SUMMARY FOR {month} ---")
    show_summary(monthly)


def main():
    transactions = load_transactions()

    while True:
        print("\n=== PERSONAL FINANCE TRACKER ===")
        print("1. Add transaction")
        print("2. View transactions")
        print("3. View financial summary")
        print("4. View monthly summary")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_transaction(transactions)
        elif choice == "2":
            view_transactions(transactions)
        elif choice == "3":
            show_summary(transactions)
        elif choice == "4":
            show_monthly_summary(transactions)
        elif choice == "5":
            save_transactions(transactions)
            print("Transactions saved. Goodbye!")
            break
        else:
            print("Invalid option. Choose 1 to 5.")


if __name__ == "__main__":
    main()
