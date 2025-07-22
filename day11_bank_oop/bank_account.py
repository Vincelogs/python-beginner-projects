# bank_account.py

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"✅ Deposited ₦{amount}. New balance: ₦{self.balance}")
        else:
            print("❌ Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"✅ Withdrew ₦{amount}. New balance: ₦{self.balance}")
        else:
            print("❌ Insufficient balance.")

    def get_balance(self):
        print(f"📊 Current balance: ₦{self.balance}")

# Run the app
print("=== Welcome to Python Bank 🏦 ===")
name = input("Enter your name: ")
account = BankAccount(name)

while True:
    print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)
    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)
    elif choice == "3":
        account.get_balance()
    elif choice == "4":
        print("Thank you for banking with us, goodbye!")
        break
    else:
        print("❌ Invalid option.")
