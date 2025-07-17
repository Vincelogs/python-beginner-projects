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


### 📢 LinkedIn Post Template:

> 🎯 **Day 10: Python Quiz App with Error Handling**
>
> Today I learned how to **make my programs unbreakable** by handling errors the right way:
>
> * Caught bad user input with `try/except`
> * Prevented crashes from division by zero and invalid types
> * Made my app more **resilient and user-friendly**
>
> To practice, I built a fun little **Python Quiz App**:
>
> ```python
> try:
>     answer = input("Question: ")
> except Exception as e:
>     print("⚠️ Error:", e)
> ```
>
> Whether the user gives the right answer, wrong one, or nothing at all — the app stays alive 💪
>
> Code on GitHub 👉 \[insert repo link]
>
> \#Python #Day10 #ErrorHandling #QuizApp #ResilientCode #VincentLearns #ZeroToDev #BuildInPublic
