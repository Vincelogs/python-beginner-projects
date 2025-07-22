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



### 📢 LinkedIn Post Template:

> 🔐 **Day 13 of My Python Dev Journey: User Login System (OOP Inheritance)**
>
> Today I tackled **Inheritance** in Python.
> I learned how to:
>
> * Build parent & child class structures
> * Use `super()` to initialize base class
> * Simulate real systems with multiple user types
>
> I built a **Login System** with:
>
> * Standard users
> * Admin users (with permission to view all accounts)
>
> Sample code:
>
> ```python
> class Admin(User):
>     def view_all_users(self, users):
>         for user in users:
>             print(user.username)
> ```
>
> OOP is starting to feel like real-life modeling — and I’m loving it 🔥
>
> Code is on GitHub 👉 \[insert repo link]
>
> \#Python #Day13 #LoginSystem #Inheritance #OOP #VincentLearns #BuildInPublic #ZeroToDev #TechJourney
