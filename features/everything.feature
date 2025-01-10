# everything.feature

Feature: Manage tasks in the to-do list

  Scenario: Add a task to the to-do list
    Given the to-do list is empty
    When the user adds a task "Buy sweets"
    Then the to-do list should contain "Task 'Buy sweets' added with ID 1 and priority Low."

  Scenario: List all tasks in the to-do list
    Given the to-do list contains the tasks: ID 1: Buy sweets, ID 2: Pay bills
    When the user lists all tasks
    Then the output should contain: "ID 1: Buy sweets - Pending - Priority: Medium,ID 2: Pay bills - Pending - Priority: High"

  Scenario: Mark a task as completed
    Given the to-do list contains the task: Buy sweets – Pending
    When the user completes the task "Buy sweets"
    Then the to-do list should show the task "Buy sweets" as completed

  Scenario: Create a task and assign priority
    Given the to-do list is empty
    When the user adds a task: "Pay bills" and assigns priority Medium
    Then the to-do list should contain: "Task 'Pay bills' added with ID 1 and priority Medium."

  Scenario: Edit an existing task's name and priority
    Given the to-do list contains the task edit: ID 1: Buy sweets - Pending - Priority: Low
    When the user edits task ID 1 to change the name to "Buy chocolates" and the priority to "High"
    Then the to-do list should contain the task "Buy chocolates" with ID 1 and priority High

  Scenario: Delete a task from the to-do list
    Given the to-do list contains the tasks: ID 1: Buy sweets, ID 2: Pay bills
    When the user deletes the task with ID 1
    Then the to-do list should contain only "ID 2: Pay bills"

  Scenario: Clear the entire to-do list
    Given the to-do list contains the tasks: Buy sweets, Pay bills
    When the user clears the to-do list
    Then the to-do list should be empty

