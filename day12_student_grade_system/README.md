## 🐍 **Day 12: OOP – Student Grade System**
### 📘 What You Learn:

* How to model real-world systems with multiple data points
* OOP with lists and conditional logic
* Making your class more intelligent with methods

---

### 🧠 Concepts Recap:

```python
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, score):
        self.grades.append(score)

    def average(self):
        return sum(self.grades) / len(self.grades)

    def grade_status(self):
        avg = self.average()
        if avg >= 70:
            return "🟢 Distinction"
        elif avg >= 50:
            return "🟡 Pass"
        else:
            return "🔴 Fail"
```

---

### 🛠️ Mini Project: **Student Grade Management System 🎓**



