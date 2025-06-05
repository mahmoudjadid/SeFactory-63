
# checklist_app.py

tasks = []

def show_menu():
    print("\nTo-Do Checklist")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "done": False})
    print("Task added!")

def view_tasks():
    if not tasks:
        print("No tasks yet.")
        return
    for i, t in enumerate(tasks, start=1):
        status = "[x]" if t["done"] else "[ ]"
        print(f"{status} {i}. {t['task']}")

# Main program loop
while True:
    show_menu()
    choice = input("Choose an option (1-3): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")




