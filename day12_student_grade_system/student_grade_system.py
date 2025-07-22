# student_grade_system.py

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            print("❌ Invalid grade. Must be between 0 and 100.")

    def calculate_average(self):
        if not self.grades:
            return 0
        return round(sum(self.grades) / len(self.grades), 2)

    def get_status(self):
        avg = self.calculate_average()
        if avg >= 70:
            return "🟢 Distinction"
        elif avg >= 50:
            return "🟡 Pass"
        else:
            return "🔴 Fail"

# Run App
print("=== Student Grade System 🎓 ===")
student_name = input("Enter student name: ")
student = Student(student_name)

while True:
    print("\n1. Add Grade\n2. Show Average\n3. Show Status\n4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        try:
            grade = float(input("Enter grade (0 - 100): "))
            student.add_grade(grade)
        except ValueError:
            print("❌ Please enter a valid number.")
    elif choice == "2":
        avg = student.calculate_average()
        print(f"📊 {student.name}'s average grade: {avg}")
    elif choice == "3":
        print(f"📈 {student.name}'s result: {student.get_status()}")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("❌ Invalid option.")
