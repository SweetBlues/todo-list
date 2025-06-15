tasks = []

def show_menu():
    print("\nTo-Do List")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added!")
    elif choice == "2":
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    elif choice == "3":
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    to_delete = int(input("Enter task number to delete: "))
    if 0 < to_delete <= len(tasks):
        removed = tasks.pop(to_delete - 1)
        print(f"Deleted: {removed}")
    else:
        print("Invalid task number.")
    elif choice == "4":
    print("Goodbye!")
    break
    else:
        print("Invalid choice, try again.")