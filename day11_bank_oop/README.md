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

