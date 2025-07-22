## 🐍 **Day 11: Classes & Objects (OOP in Python)**

### 📘 What You Learn:

* What OOP is and why it's powerful
* Creating your own **classes** and **objects**
* `__init__()` constructor and instance methods
* Simulating real-world entities using Python

---

### 🧠 Concepts:

```python
# Define a class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I’m {self.age} years old.")

# Create an object
vincent = Person("Vincent", 26)
vincent.greet()  # Output: Hello, my name is Vincent and I’m 26 years old.
```

---

### 🛠️ Mini Project: **Bank Account System 🏦**


### 📢 LinkedIn Post Template:

> 🏦 **Day 11: Python OOP – Bank Account Simulation**
>
> Today I officially entered the world of **Object-Oriented Programming (OOP)** in Python.
> I learned how to:
>
> * Create classes & objects
> * Use constructors and instance methods
> * Simulate real-world systems (like banking 💸)
>
> I built a full **Bank Account System** that allows you to:
>
> * Deposit
> * Withdraw
> * Check balance
>
> Sample snippet:
>
> ```python
> class BankAccount:
>     def __init__(self, owner, balance=0):
>         self.owner = owner
>         self.balance = balance
> ```
>
> This is a BIG leap in writing clean, structured, and scalable code.
>
> GitHub code 👉 \[insert repo link]
>
> \#Python #OOP #Day11 #BankApp #FromZeroToDev #VincentLearns #BuildInPublic #ClassesAndObjects

