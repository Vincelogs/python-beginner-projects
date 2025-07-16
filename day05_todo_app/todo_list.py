# todo_list.py

tasks = []

def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        if tasks:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("No tasks yet.")
    
    elif choice == "2":
        new_task = input("Enter a new task: ")
        tasks.append(new_task)
        print("Task added.")
    
    elif choice == "3":
        task_num = int(input("Enter task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")
    
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
