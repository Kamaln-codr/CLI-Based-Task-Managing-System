import json

tsk = []

def save_tasks():
    with open("tasks.json", "w") as f:
        json.dump(tsk, f)

def load_tasks():
    global tsk
    try:
        with open("tasks.json", "r") as f:
            tsk = json.load(f)
    except FileNotFoundError:
        tsk = []

def addtask(task_name):
    tsk.append(task_name)
    save_tasks()
    print(f'"{task_name}" added as a task')

def deltask(task_name):
    if task_name in tsk:
        tsk.remove(task_name)
        save_tasks()
        print(f"Task '{task_name}' removed from the list")
    else:
        print("Task not found.")

def editask(task_index, new_task):
    if 0 <= task_index < len(tsk):
        old_task = tsk[task_index]
        tsk[task_index] = new_task
        save_tasks()
        print(f"The task '{old_task}' has now been replaced with '{new_task}'")
    else:
        print("Invalid task index.")

def showtask():
    print("---------Your Tasks---------")
    for i, task in enumerate(tsk, 1):
        print(f"{i}. {task}")
    print("----------------------------")

# Main loop
load_tasks()
print("Welcome to the To-do List Tracker App.")
print("Choose an option:\n1 → Add task\n2 → Edit task\n3 → Delete task\n4 → Show tasks\n5 → Exit")

while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        task_name = input("Enter your task: ")
        addtask(task_name)
    elif choice == 2:
        showtask()
        task_index = int(input("Enter task index to edit: ")) - 1
        new_task = input("Enter the new task: ")
        editask(task_index, new_task)
    elif choice == 3:
        task_name = input("Enter the task name to delete: ")
        deltask(task_name)
    elif choice == 4:
        showtask()
    elif choice == 5:
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
        continue
