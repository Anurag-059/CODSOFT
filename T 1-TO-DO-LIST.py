import json
import os

TODO_FILE = 'todo_list.json'

def load_todo_list():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as f:
            return json.load(f)
    return []

def save_todo_list(todo_list):
    with open(TODO_FILE, 'w') as f:
        json.dump(todo_list, f, indent=4)

def add_task(todo_list, task):
    todo_list.append({"task": task, "done": False})
    save_todo_list(todo_list)

def update_task(todo_list, index, new_task):
    if 0 <= index < len(todo_list):
        todo_list[index]["task"] = new_task
        save_todo_list(todo_list)

def delete_task(todo_list, index):
    if 0 <= index < len(todo_list):
        del todo_list[index]
        save_todo_list(todo_list)

def mark_task_done(todo_list, index):
    if 0 <= index < len(todo_list):
        todo_list[index]["done"] = True
        save_todo_list(todo_list)

def view_tasks(todo_list):
    for i, task in enumerate(todo_list):
        status = "Done" if task["done"] else "Not Done"
        print(f"{i+1}. {task['task']} [{status}]")

def main():
    todo_list = load_todo_list()
    while True:
        print("\nTo-Do List Application")
        print("1. View tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Delete task")
        print("5. Mark task as done")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            view_tasks(todo_list)
        elif choice == '2':
            task = input("Enter the new task: ")
            add_task(todo_list, task)
        elif choice == '3':
            index = int(input("Enter the task number to update: ")) - 1
            new_task = input("Enter the updated task: ")
            update_task(todo_list, index, new_task)
        elif choice == '4':
            index = int(input("Enter the task number to delete: ")) - 1
            delete_task(todo_list, index)
        elif choice == '5':
            index = int(input("Enter the task number to mark as done: ")) - 1
            mark_task_done(todo_list, index)
        elif choice == '6':
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "_main_":
    main()