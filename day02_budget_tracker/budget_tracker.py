# budget_tracker.py

print("=== Daily Budget Tracker ===")

income = float(input("Enter your daily income: ₦"))
food = float(input("Food expenses: ₦"))
transport = float(input("Transport: ₦"))
others = float(input("Others: ₦"))

total_expense = food + transport + others
balance = income - total_expense

print("\nTotal Expense: ₦", total_expense)
print("Balance: ₦", balance)

if balance < 0:
    print("⚠️ You overspent today.")
elif balance == 0:
    print("You broke even.")
else:
    print("✅ You're within budget. Good job!")
