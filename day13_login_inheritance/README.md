## 🐍 **Day 13: OOP – Inheritance + User Login System**

### 📘 What You Learn:

* **Inheritance** in Python classes
* `super()` for accessing parent methods
* Creating base + child class relationships
* Real-world simulation of login logic

---

### 🧠 Concepts:

```python
class User:
    def __init__(self, username):
        self.username = username

    def login(self):
        print(f"{self.username} has logged in.")

class Admin(User):
    def access_admin_panel(self):
        print(f"Admin {self.username} is accessing admin panel.")

# Usage
u1 = User("john")
u1.login()  # john has logged in

a1 = Admin("vincent")
a1.login()  # vincent has logged in
a1.access_admin_panel()
```

---

### 🛠️ Mini Project: **User Login System (with Inheritance)**
