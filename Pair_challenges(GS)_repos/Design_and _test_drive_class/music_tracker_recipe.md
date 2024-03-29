# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._
As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.


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
class music_tracker:

    def __init__(self, list):
    #Parameters:
    #  list: []
    # Side effects:
    #   Sets the name property of the self object

    def add(self, songs):
    #Parameters:
    #    song: string
    # string representing a song
    # task:adds the song to the self list
    #returns: nothing

    def view_list(self):
    # task: Shows the list of added songs
    #returns: list of songs


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
Given a song 
Returns it in the list
"""
track = music_tracker(list)
track.add("let it go!")
track.view_list() => list = ["let it go!"]

"""
Given an empty song argument
Returns "Please enter a song title"
"""
track = music_tracker(list)
track.add("")
track.view_list() => "Please enter a song title"

"""
Given you view the list before adding any songs
Return should be empty
"""
track.view_list() => list = []

"""
Given you add more songs
Return more than one song in list 
"""
track = music_tracker(list)
track.add("let it go!")
track.view_list() => list = ["let it go!"]

track.add("Hakuna matata")
track.view_list() => list = ["let it go!", "Hakuna matata"]

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
