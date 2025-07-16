## 🐍 **Day 6: File Handling in Python**

### 📘 What You Learn:

* Open, read, write, and append to files in Python
* Working with `.txt` files
* Using `with` blocks for file safety
* Real-world use case: storing to-do tasks to disk

---

### 🧠 Concepts:

```python
# Writing to a file
with open("notes.txt", "w") as file:
    file.write("Python is awesome!\n")

# Reading from a file
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)

# Appending to a file
with open("notes.txt", "a") as file:
    file.write("Keep learning!\n")
```

---

### 🛠️ Mini Project: **Persistent To-Do List (File Storage) 📝**
