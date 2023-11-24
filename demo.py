# Menu for the user
print("Task List Manager")
print("\n1. Add Task")
print("2. View Tasks")
print("3. Mark Task as Completed")
print("4. Delete Task")
print("5. Quit")


# Just declare the active for the WHILE loop
active = True

# This is an empty dictionary to house the user tasks
task_list = {}

# This is an empty list to house completed tasks
compl_task = []

# loop for the task
while active:
    # This is the input message
    input_message = input("\nEnter your choice: ")

    # Convert input_message to int
    input_message = int(input_message)

    if input_message == 1:
        get_task = input("Enter task name: ")
        due_date = input("Enter due date (DD-MM-YYYY): ")
        due_date = str(due_date)

        # Add task to the task_list dictionary
        task_list[len(task_list) + 1] = {'name': get_task, 'due_date': due_date, 'completed': False}
        print("Task added successfully!")

    elif input_message == 2:
        print("\nTask List:")
        for task_number, task_details in task_list.items():
            status = " - Completed" if task_details['completed'] else ""
            print(f"{task_number}. {task_details['name']} (Due {task_details['due_date']}){status}")

    elif input_message == 3:
        task_number_to_complete = int(input("Enter the task number to mark as completed: "))
        if task_number_to_complete in task_list:
            task_list[task_number_to_complete]['completed'] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number. Please try again.")

    elif input_message == 4:
        task_number_to_delete = int(input("Enter the task number to delete: "))
        if task_number_to_delete in task_list:
            deleted_task = task_list.pop(task_number_to_delete)
            compl_task.append(deleted_task)
            print("Task deleted successfully!")
        else:
            print("Invalid task number. Please try again.")

    elif input_message == 5:
        print("Exiting Task List Manager. Goodbye!")
        active = False

    else:
        print("Invalid choice. Please enter a valid option.")
