class Task:
    def __init__(self, title, description, priority, due_date):
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.completed = False

class TaskManager:
    def __init__(self):
        self.task_list = []

    def add_task(self, task):
        self.task_list.append(task)
    
    def remove_task(self, task_index):
        if 0 <= task_index < len(self.task_list):
            self.task_list.pop(task_index)
                
    def mark_task_complete(self, task_index):
        if 0 <= task_index < len(self.task_list):
            self.task_list[task_index].completed = True
    
    def show_tasks(self):
        if len(self.task_list) == 0:
            print("No tasks to show!")
            return
        
        for index, task in enumerate(self.task_list):
            status = "Complete" if task.completed else "Incomplete"
            print(f"{index + 1}. {task.title} - Priority: {task.priority} - Due Date: {task.due_date} - Status: {status}")

def main():
    task_manager = TaskManager()

    while True:
        print("\nText-Based Task Manager")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. Show Tasks")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            priority = input("Enter task priority (High/Medium/Low): ")
            due_date = input("Enter task due date: ")
            new_task = Task(title, description, priority, due_date)
            task_manager.add_task(new_task)
            print("Task added successfully!")

        elif choice == "2":
            task_manager.show_tasks()
            task_index = int(input("Enter the task number to mark as complete: ")) - 1
            task_manager.mark_task_complete(task_index)
            print("Task marked as complete!")

        elif choice == "3":
            task_manager.show_tasks()

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()





