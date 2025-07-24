def main():
    while True:
        print("\n=== Python Week 2 Toolkit ===")
        print("1. Weather Checker")
        print("2. Student Grade Manager")
        print("3. User Login System")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            import smart_weather_checker
        elif choice == "2":
            import student_grade_system
        elif choice == "3":
            import login_system
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()