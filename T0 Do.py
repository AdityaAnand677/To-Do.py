# Simple To-Do List Application

tasks = []

while True:
    print("\n----- TO DO LIST MENU -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter new task: ")
        tasks.append({"task": task, "done": False})
        print("Task added successfully!")

    elif choice == '2':
        if len(tasks) == 0:
            print("No tasks in the list.")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(tasks):
                status = "Done" if t["done"] else "Not Done"
                print(f"{i+1}. {t['task']} [{status}]")

    elif choice == '3':
        task_no = int(input("Enter task number to mark completed: "))
        if 0 < task_no <= len(tasks):
            tasks[task_no-1]["done"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number")

    elif choice == '4':
        task_no = int(input("Enter task number to delete: "))
        if 0 < task_no <= len(tasks):
            tasks.pop(task_no-1)
            print("Task deleted successfully!")
        else:
            print("Invalid task number")

    elif choice == '5':
        print("Exiting To-Do List App")
        break

    else:
        print("Invalid choice. Try again.")
