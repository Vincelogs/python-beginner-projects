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



### 📢 LinkedIn Post Template:

> 🎓 **Day 12 of My Python Dev Journey: Student Grade System (OOP)**
>
> Today I leveled up in **Object-Oriented Programming** by building a real-world **Student Grade Manager** using Python.
>
> ✅ Add multiple grades
> ✅ Calculate average
> ✅ Return pass/fail/distinction status
>
> Sample snippet:
>
> ```python
> def get_status(self):
>     avg = self.calculate_average()
>     if avg >= 70:
>         return "Distinction"
> ```
>
> This felt like building a mini report card engine. 💼
>
> GitHub 👉 \[insert repo link]
>
> \#Python #OOP #StudentGrades #Day12 #FromZeroToDev #VincentLearns #BuildInPublic #ConsoleApp #TechJourney
