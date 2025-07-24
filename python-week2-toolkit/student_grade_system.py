class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            print("Invalid grade. Must be 0-100.")

    def average(self):
        return round(sum(self.grades) / len(self.grades), 2) if self.grades else 0

    def status(self):
        avg = self.average()
        if avg >= 70:
            return "Distinction"
        elif avg >= 50:
            return "Pass"
        else:
            return "Fail"

name = input("Enter student name: ")
student = Student(name)

while True:
    print("\n1. Add Grade\n2. Show Average\n3. Show Status\n4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        try:
            grade = float(input("Enter grade: "))
            student.add_grade(grade)
        except ValueError:
            print("Invalid input. Enter a number.")
    elif choice == "2":
        print(f"Average: {student.average()}")
    elif choice == "3":
        print(f"Status: {student.status()}")
    elif choice == "4":
        break
    else:
        print("Invalid option.")