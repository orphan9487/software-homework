import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"
FIELDNAMES = ["date", "amount", "category", "notes"]


def init_file():
    """Initialize CSV file with header if it does not exist."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()


def get_date():
    while True:
        date_str = input("Enter date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")


def get_amount():  # 金額輸入
    while True:
        try:
            amount = float(input("Enter amount: ").strip())
            if amount <= 0:
                raise ValueError
            return amount
        except ValueError:
            print("Amount must be a positive number.")


def get_category():  # 類別輸入
    while True:
        category = input("Enter category: ").strip()
        if category:
            return category
        print("Category cannot be empty.")


def get_notes():  # 備註 (選填)
    return input("Enter notes (optional): ").strip()


def add_expense():  # 整合用
    expense = {
        "date": get_date(),
        "amount": get_amount(),
        "category": get_category(),
        "notes": get_notes()
    }

    with open(FILE_NAME, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writerow(expense)

    print("Expense added successfully.\n")


def main():
    init_file()
    print("=== Expense Input Module ===")

    while True:  # 可以連續輸入多筆資料
        add_expense()
        cont = input("Add another expense? (y/n): ").strip().lower()
        if cont != "y":
            break


if __name__ == "__main__":
    main()
