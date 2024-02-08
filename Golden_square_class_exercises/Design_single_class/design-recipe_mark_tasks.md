# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

class attributes should be 
class methods should include adding tasks, showing the incomplete tasks, then marking off a completed class

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

class mark_tasks:
    def add_task(self, task):
    # parameters = a string representing a single task
    # return added task to the self.task_list 
    # side effects: if task is not a string return error message 
    #  if task is empty return error message
        pass
    def incomplete_tasks(self):
    # return self.task_list
    # side effects: if list is empty return error message
        pass

    def complete_tasks(self, completed):
    # completed is the index/ the task that will be removed #from the list


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

_Encode each example as a test. You can add to the above list as you go._

```python

"""
when presenting incomplete tasks- the list should be empty
"""
mark = mark_tasks()
mark.incomplete_tasks() => []

"""
When we add a task it is reflected in the incompleted taks list
"""
mark = mark_tasks()
mark.add_task("Feed the cat.")
mark.incomplete_tasks() => ["Feed the cat."]

"""
When adding multiple tasks it is added to list
and refelct in incompleted meth
"""
mark = mark_tasks()
mark.add_task("Feed the cat.")
mark.add_task("Feed the fish.")
mark.incomplete_tasks() => ["Feed the cat.","Feed the fish."]

mark = mark_tasks()
mark.add_task("Feed the cat.")
mark.add_task("Feed the fish.")
mark.add_task("Feed the lion.")
mark.incomplete_tasks() => ["Feed the cat.","Feed the fish.","Feed the lion."]

"""
When indexing a num in the completed tasks method
It removes that indexed task from the list
"""
mark = mark_tasks()
mark.add_task("Feed the cat.")
mark.add_task("Feed the fish.")
mark.add_task("Feed the lion.")
mark.complete_tasks(1)
mark.incomplete_tasks() => ["Feed the cat.","Feed the lion."]

"""
If we try to to mark a task out of the range of the list (too low)
error message will be shown
"""
mark = mark_tasks()
mark.add_task("Feed the cat.")
mark.add_task("Feed the fish.")
mark.add_task("Feed the lion.")
mark.complete_tasks(-3) => #raises an error message "Out of list range"
mark.incomplete_tasks() => ["Feed the cat.","Feed the fish.","Feed the lion."]

"""
If we try to to mark a task out of the range of the list (too high)
error message will be shown
"""
mark = mark_tasks()
mark.add_task("Feed the cat.")
mark.add_task("Feed the fish.")
mark.add_task("Feed the lion.")
mark.complete_tasks(6) => #raises an error message "Out of list range"
mark.incomplete_tasks() => ["Feed the cat.","Feed the fish.","Feed the lion."]
```

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

