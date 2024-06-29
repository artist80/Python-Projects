# Simple To-Do List App in Python

tasks = []

def display_menu():
    print("\nTo-Do List Application")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Delete a task")
    print("4. Exit")

def view_tasks():
    if not tasks:
        print("\nNo tasks in the list.")
    else:
        print("\nTasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def add_task():
    task = input("\nEnter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")

def delete_task():
    if not tasks:
        print("\nNo tasks to delete.")
    else:
        view_tasks()
        try:
            task_number = int(input("\nEnter the task number to delete: "))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Task '{removed_task}' removed from the list.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    while True:
        display_menu()
        choice = input("\nChoose an option: ")
        
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("\nExiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
