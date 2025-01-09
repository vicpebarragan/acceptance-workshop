
import io
import contextlib
from behave import given, when, then
from todo import add_task, list_tasks, clear_tasks, mark_task_completed, edit_task, delete_task

# Global dictionary to simulate the to-do list in memory
task_list = {}

# Step 1: Given the to-do list is empty
@given('the to-do list is empty')
def step_given_list_is_empty(context):
    global task_list
    task_list = {}

# Step 2: When the user adds a task "{task_name}"
@when('the user adds a task "{task_name}"')
def step_when_user_adds_task(context, task_name):
    f = io.StringIO()
    with contextlib.redirect_stdout(f):
        add_task(task_list, task_name, 'Low')
    context.output = f.getvalue().strip()

# Step 3: Then the to-do list should contain "{expected_task}"
@then('the to-do list should contain "{expected_task}"')
def step_then_list_should_contain(context, expected_task):
    assert context.output == expected_task




# Step 4: Given the to-do list contains the tasks: ID 1: Buy sweets, ID 2: Pay bills
@given('the to-do list contains the tasks: ID 1: {task1}, ID 2: {task2}')
def step_given_list_with_tasks(context, task1, task2):
    global task_list
    task_list = {
        1: {'name': task1, 'completed': False, 'priority': 'Medium'},
        2: {'name': task2, 'completed': False, 'priority': 'High'}
    }

# Step 5: When the user lists all tasks
@when('the user lists all tasks')
def step_when_user_lists_tasks(context):
    f = io.StringIO()
    with contextlib.redirect_stdout(f):
        list_tasks(task_list)
    context.output = f.getvalue().strip()
    print(context.output)

# Step 6: Then the output should contain "{expected_tasks}"
@then('the output should contain: "{expected_tasks}"')
def step_then_output_should_contain(context, expected_tasks):
    expected_tasks = expected_tasks.replace(',', '\n')  # Ensure consistent formatting
    assert context.output == expected_tasks



# Step 7: Given the to-do list contains the task: {task} - Pending
@given('the to-do list contains the task: {task} - Pending')
def step_given_list_with_one_task(context, task):
    global task_list
    task_list = {1: {'name': task, 'completed': False, 'priority': 'Low'}}

# Step 8: When the user completes the task "{task_name}"
@when('the user completes the task "{task_name}"')
def step_when_user_completes_task(context, task_name):
    task_id = next(id for id, task in task_list.items() if task['name'] == task_name)
    mark_task_completed(task_list, task_id)

# Step 9: Then the to-do list should show the task "{task_name}" as completed
@then('the to-do list should show the task "{task_name}" as completed')
def step_then_task_should_be_completed(context, task_name):
    task_id = next(id for id, task in task_list.items() if task['name'] == task_name)
    assert task_list[task_id]['completed'] is True




# Step 10: Given the to-do list contains the tasks: {task1}, {task2}
@given('the to-do list contains the tasks: {task1}, {task2}')
def step_given_list_to_clean(context, task1, task2):
    global task_list
    task_list = {
        1: {'name': task1, 'completed': False, 'priority': 'Medium'},
        2: {'name': task2, 'completed': False, 'priority': 'High'}
    }

# Step 11: When the user clears the to-do list
@when('the user clears the to-do list')
def step_when_user_clears_list(context):
    clear_tasks(task_list)

# Step 12: Then the to-do list should be empty
@then('the to-do list should be empty')
def step_then_list_should_be_empty(context):
    assert not task_list

# Step 13: Given the to-do list is empty
@given('the to-do list is empty 2')
def step_given_empty_list_priority(context):
    global task_list
    task_list = {}

# Step 14: When the user adds a task: "{task_name}" and assigns priority {priority}
@when('the user adds a task: "{task_name}" and assigns priority {priority}')
def step_when_user_adds_task_with_priority(context, task_name, priority):
    f = io.StringIO()
    with contextlib.redirect_stdout(f):
        add_task(task_list, task_name, priority)
    context.output = f.getvalue().strip()

# Step 15: Then the to-do list should contain: "{expected_task}"
@then('the to-do list should contain: "{expected_task}"')
def step_then_list_should_contain_with_priority(context, expected_task):
    assert context.output == expected_task

# Step 16: When the user edits task ID {task_id} to change the name to "{new_name}" and the priority to "{new_priority}"
@when('the user edits task ID {task_id} to change the name to "{new_name}" and the priority to "{new_priority}"')
def step_when_user_edits_task(context, task_id, new_name, new_priority):
    f = io.StringIO()
    with contextlib.redirect_stdout(f):
        edit_task(task_list, task_id, new_name, new_priority)
    context.output = f.getvalue().strip()

# Step 17: Then the to-do list should contain the task "{new_name}" with ID {task_id} and priority {new_priority}
@then('the to-do list should contain the task "{new_name}" with ID {task_id} and priority {new_priority}')
def step_then_task_should_be_updated(context, new_name, task_id, new_priority):
    task = task_list[task_id]
    assert task['name'] == new_name, f"Expected task name to be '{new_name}', but got '{task['name']}'"
    assert task['priority'] == new_priority, f"Expected priority to be '{new_priority}', but got '{task['priority']}'"

# Step 18: When the user deletes the task with ID {task_id}
@when('the user deletes the task with ID {task_id}')
def step_when_user_deletes_task(context, task_id):
    f = io.StringIO()
    with contextlib.redirect_stdout(f):
        delete_task(task_list, task_id)
    context.output = f.getvalue().strip()

# Step 19: Then the to-do list should contain only "{remaining_tasks}"
@then('the to-do list should contain only "{remaining_tasks}"')
def step_then_list_should_contain_only_remaining_tasks(context, remaining_tasks):
    remaining_task_names = [task['name'] for task in task_list.values()]
    assert ', '.join(remaining_task_names) == remaining_tasks, f"Expected remaining tasks: {remaining_tasks}, but got: {', '.join(remaining_task_names)}"
