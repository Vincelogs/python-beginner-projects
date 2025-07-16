# expense_manager.py

FILENAME = "expenses.txt"

def save_expense(date, total, income):
    with open(FILENAME, "a") as file:
        file.write(f"{date} - Income: ₦{income} | Spent: ₦{total}\n")

def view_history():
    try:
        with open(FILENAME, "r") as file:
            print("\n--- Expense History ---")
            print(file.read())
    except FileNotFoundError:
        print("No expense history yet.")

print("=== Daily Expense Manager ===")
while True:
    print("\n1. Add New Expense")
    print("2. View Expense History")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        import datetime
        date = datetime.datetime.now().strftime("%Y-%m-%d")

        income = float(input("Enter your daily income (₦): "))
        food = float(input("Food expense: ₦"))
        transport = float(input("Transport: ₦"))
        others = float(input("Others: ₦"))

        total = food + transport + others
        balance = income - total

        print(f"Total spent today: ₦{total}")
        print(f"Balance: ₦{balance}")

        if balance < 0:
            print("⚠️ Overspending alert!")
        elif balance == 0:
            print("You broke even.")
        else:
            print("✅ You're within budget!")

        save_expense(date, total, income)

    elif choice == "2":
        view_history()

    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")
