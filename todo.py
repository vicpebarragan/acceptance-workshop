def add_task(task_list, task_name, priority):
    """Add a new task to the list."""

    if priority not in ['High', 'Medium', 'Low']:
        print("Invalid priority. It must be 'High', 'Medium' or 'Low'.")
        return

    task_id = len(task_list) + 1
    task_list[task_id] = {
        'name': task_name,
        'completed': False,
        'priority': priority,
    }
    print(f"Task '{task_name}' added with ID {task_id} and priority {priority}.")

def list_tasks(task_list):
    """List all the tasks."""
    if not task_list:
        print("There are no tasks on the list.")
    else:
        for task_id, task_info in task_list.items():
            status = "Completed" if task_info['completed'] else "Pending"
            print(f"ID {task_id}: {task_info['name']} - {status} - Priority: {task_info['priority']}")


def mark_task_completed(task_list, task_id):
    """Mark a task as completed."""
    if task_id in task_list:
        task_list[task_id]['completed'] = True
        print(f"Task ID {task_id} marked as completed.")
    else:
        print(f"Task with ID not found {task_id}.")

def clear_tasks(task_list):
    """Clean all the tasks."""
    task_list.clear()
    print("All tasks have been deleted.")


def edit_task(task_list, task_id):
    """Edit the name or priority of an existing task."""
    if task_id in task_list:
        print(f"Editing Task ID {task_id}: {task_list[task_id]['name']}")
        new_name = input("Enter new name (leave blank to keep current name): ")
        new_priority = input("Enter new priority (High, Medium, Low) or leave blank to keep current: ")

        if new_name:
            task_list[task_id]['name'] = new_name

        if new_priority and new_priority in ['High', 'Medium', 'Low']:
            task_list[task_id]['priority'] = new_priority

        print(f"Task ID {task_id} updated successfully.")
    else:
        print(f"Task with ID {task_id} not found.")


def delete_task(task_list, task_id):
    """Delete a specific task."""
    if task_id in task_list:
        del task_list[task_id]
        print(f"Task ID {task_id} has been deleted.")
    else:
        print(f"Task with ID {task_id} not found.")

def main():
    """Main function to run the application."""
    task_list = {}
    
    while True:
        print("\n--- Task Manager ---")
        print("1. Add new task")
        print("2. List all tasks")
        print("3. Clear all tasks")
        print("4. Mark task as completed")
        print("5. Edit task")
        print("6. Delete task")
        print("7. Exit")
        
        choice = input("Select an option (1-7): ")
        
        if choice == '1':
            task_name = input("Enter the task name: ")
            priority = input("Enter the task priority (High, Medium, Low): ")
            add_task(task_list, task_name, priority)
        elif choice == '2':
            list_tasks(task_list)
        elif choice == '3':
            clear_tasks(task_list)
        elif choice == '4':
            try:
                task_id = int(input("Enter the task ID to mark as completed: "))
                mark_task_completed(task_list, task_id)
            except ValueError:
                print("Invalid task ID.")
        elif choice == '5':
            try:
                task_id = int(input("Enter the task ID to edit: "))
                edit_task(task_list, task_id)
            except ValueError:
                print("Invalid task ID.")
        elif choice == '6':
            try:
                task_id = int(input("Enter the task ID to delete: "))
                delete_task(task_list, task_id)
            except ValueError:
                print("Invalid task ID.")
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please select an option between 1 and 7.")

if __name__ == "__main__":
    main()
