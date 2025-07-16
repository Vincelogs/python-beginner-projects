# tip_calculator.py

def calculate_tip(bill_amount, tip_percent):
    tip = bill_amount * (tip_percent / 100)
    total = bill_amount + tip
    return round(tip, 2), round(total, 2)

print("=== Tip Calculator ===")
bill = float(input("Enter your bill amount (₦): "))
tip_percent = float(input("Enter tip percentage (%): "))

tip, total = calculate_tip(bill, tip_percent)

print(f"\nTip: ₦{tip}")
print(f"Total to Pay: ₦{total}")