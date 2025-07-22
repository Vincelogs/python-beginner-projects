## 🐍 **Day 10: Error Handling + Quiz App**

### 📘 What You Learn:

* How to handle runtime errors using `try`, `except`, `finally`
* Using `else` in try-blocks for clean logic
* Building programs that don’t crash
* Writing user-friendly and defensive code

---

### 🧠 Concepts:

```python
# Basic error handling
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("❌ Can't divide by zero.")
except ValueError:
    print("❌ Please enter a valid number.")
finally:
    print("✅ Done trying.")

# Optional: use else
try:
    result = 10 / 2
except:
    print("Error!")
else:
    print("No error occurred.")
```

---

### 🛠️ Mini Project: **Python Quiz App with Error Handling 🎯**


