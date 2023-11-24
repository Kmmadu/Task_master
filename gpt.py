class TaskListManager:
    def __init__(self):
        self.tasks = {}

    def add_task(self):
        task_name = input("Enter task name: ")
        due_date = input("Enter due date (YYYY-MM-DD): ")
        task_id = len(self.tasks) + 1
        self.tasks[task_id] = {'name': task_name, 'due_date': due_date, 'completed': False}
        print("Task added successfully!")

    def view_tasks(self):
        print("Task List:")
        if not self.tasks:
            print("(Empty)")
        else:
            for task_id, task_details in self.tasks.items():
                status = " - Completed" if task_details['completed'] else ""
                print(f"{task_id}. {task_details['name']} (Due: {task_details['due_date']}){status}")

    def mark_completed(self):
        task_id = int(input("Enter the task number to mark as completed: "))
        if task_id in self.tasks:
            self.tasks[task_id]['completed'] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number. Please try again.")

    def delete_task(self):
        task_id = int(input("Enter the task number to delete: "))
        if task_id in self.tasks:
            del self.tasks[task_id]
            print("Task deleted successfully!")
        else:
            print("Invalid task number. Please try again.")

    def run(self):
        while True:
            print("\nTask List Manager")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Mark Task as Completed")
            print("4. Delete Task")
            print("5. Quit\n")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.add_task()
            elif choice == 2:
                self.view_tasks()
            elif choice == 3:
                self.mark_completed()
            elif choice == 4:
                self.delete_task()
            elif choice == 5:
                print("Exiting Task List Manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")


task_manager = TaskListManager()
task_manager.run()
