# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

attributes should be a list of tasks todo
methods should include adding a todo task to the list of tasks
another method should include presenting the list to the user

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class Reminder:
    # User-facing properties:
    #   name: string

    def __init__(self, name):
        # Parameters:
        #   name: string
        # Side effects:
        #   Sets the name property of the self object
        pass # No code here yet

    def remind_me_to(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the self object
        pass # No code here yet

    def remind(self):
        # Returns:
        #   A string reminding the user to do the task
        # Side-effects:
        #   Throws an exception if no task is set
        pass # No code here yet
```
```python

class todo_tasks:
     def __init__(self, task_list):
    #     self.task_list = []
    #  Parameteres- task list = empty list
        pass
    def add_task(self, task):
    # parameters = a string representing a single task
    # return added task to the self.task_list 
    # side effects: if task is not a string return error message 
    #               if task is empty return error message
        pass
    def present_tasks(self):
    # return self.task_list
    # side effects: if list is empty return error message
        pass
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a name and a task
#remind reminds the user to do the task
"""
reminder = Reminder("Kay")
reminder.remind_me_to("Walk the dog")
reminder.remind() # => "Walk the dog, Kay!"

"""
Given a name and no task
#remind raises an exception
"""
reminder = Reminder("Kay")
reminder.remind() # raises an error with the message "No task set."

"""
Given a name and an empty task
#remind still reminds the user to do the task, even though it looks odd
"""
reminder = Reminder("Kay")
reminder.remind_me_to("")
reminder.remind() # => ", Kay!"
```
```python

"""
Given a task add task to task list 
return should be added to task list
"""
todo = todo_tasks()
todo.add_task("wash the dishes.")
todo.present_tasks() => ["wash the dishes."]

"""
Given another task, 
it should be added to the list with the previous task 
"""
todo = todo_tasks()
todo.add_task("wash the dishes.")
todo.add_task("finish unit 4.")
todo.present_tasks() => ["wash the dishes.","finish unit 4."]

todo = todo_tasks()
todo.add_task("wash the dishes.")
todo.add_task("finish unit 4")
todo.add_task("go for a walk.")
todo.present_tasks() => ["wash the dishes.","finish unit 4.","go for a walk."]


"""
Given a data type other than string for add_task
should return error message
"""
todo = todo_tasks()
todo.add_task(4) => "Please add a task."

todo = todo_tasks()
todo.add_task(True) => "Please add a task."

todo = todo_tasks()
todo.add_task(5.34) => "Please add a task."

"""
when calling present_list, if the list is empty
an error message should come up
"""
todo = todo_tasks()
todo.present_tasks() => "Todo list is empty. Please add tasks"

```
_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
