# Menu for the user
print("Task List Manager")
print("\n1. Add Task")
print("2. View Tasks")
print("3. Mark Task as Completed")
print("4. Delete Task")
print("5. Quit\n")

# This is an empty list, to house the user task
task_list = {}
compl_task = []

# Just declare the active for the WHILE loop
active = True

# loop for the task
while active:

    # This is the input message
    input_message = input("Enter your choice: ")

    #Convented input_message to int 
    input_message = int(input_message)

    if input_message == 1:
        get_task = input("Enter task name: ")
        due_date = input("Enter due date (DD-MM-YYYY): ")
        due_date = str (due_date)