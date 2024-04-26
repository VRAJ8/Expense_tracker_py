import csv
import os
from datetime import datetime

def load_expenses(filename):
    expenses = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                expenses.append({'Date': row[0], 'Category': row[1], 'Amount': float(row[2])})
    return expenses

def save_expenses(expenses, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for expense in expenses:
            writer.writerow([expense['Date'], expense['Category'], expense['Amount']])

def add_expense(expenses, category, amount):
    today = datetime.now().strftime('%Y-%m-%d')
    expenses.append({'Date': today, 'Category': category, 'Amount': amount})

def view_expenses(expenses):
    total = 0
    if expenses:
        print("Date\t\tCategory\tAmount")
        print("---------------------------------------")
        for expense in expenses:
            print(f"{expense['Date']}\t{expense['Category']}\t\t{expense['Amount']}")
            total += expense['Amount']
        print("---------------------------------------")
        print(f"Total\t\t\t\t{total}")
    else:
        print("No expenses recorded yet.")

def main():
    filename = 'expenses.csv'
    expenses = load_expenses(filename)
    
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            add_expense(expenses, category, amount)
            save_expenses(expenses, filename)
            print("Expense added successfully!")
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
