# todo.py - Console-based To-Do List Application

TASKS_FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as f:
            tasks = f.read().splitlines()
    except FileNotFoundError:
        tasks = []
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("\n No tasks found!\n")
    else:
        print("\n Your To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
        print()

# Add a task
def add_task(tasks):
    task = input("Enter new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(" Task added successfully!\n")
    else:
        print(" Task cannot be empty.\n")

# Remove a task
def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            index = int(input("Enter task number to remove: ")) - 1
            if 0 <= index < len(tasks):
                removed = tasks.pop(index)
                save_tasks(tasks)
                print(f" Task '{removed}' removed successfully!\n")
            else:
                print(" Invalid task number.\n")
        except ValueError:
            print(" Please enter a valid number.\n")

# Main program loop
def main():
    tasks = load_tasks()
    
    while True:
        print("==== To-Do List Menu ====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print(" Exiting... Have a productive day!")
            break
        else:
            print(" Invalid choice! Please enter 1-4.\n")

if __name__ == "__main__":
    main()
