import pytest
from lib.add_todo_tasks import *

"""
Given a task add task to task list 
return should be added to task list
"""
def test_add_one_task():
    todo = todo_tasks()
    todo.add_task("wash the dishes.")
    assert todo.present_tasks() == ["wash the dishes."]

"""
Given another task, 
it should be added to the list with the previous task 
"""
def test_adding_second_task():
    todo = todo_tasks()
    todo.add_task("wash the dishes.")
    todo.add_task("finish unit 4.")
    assert todo.present_tasks() == ["wash the dishes.","finish unit 4."]

def test_third_added_task():
    todo = todo_tasks()
    todo.add_task("wash the dishes.")
    todo.add_task("finish unit 4.")
    todo.add_task("go for a walk.")
    assert todo.present_tasks() == ["wash the dishes.","finish unit 4.","go for a walk."]

"""
Given a data type other than string for add_task
should return error message
"""
def test_error_wrong_data_type_added_int():
    todo = todo_tasks()
    with pytest.raises(Exception) as e:
        todo.add_task(4) 
    assert str(e.value) == "Please add a task."

def test_error_wrong_data_type_added_boo():
    todo = todo_tasks()
    with pytest.raises(Exception) as err:
        todo.add_task(True) 
    assert str(err.value) == "Please add a task."

def test_error_wrong_data_type_added_float():
    todo = todo_tasks()
    with pytest.raises(Exception) as error:
        todo.add_task(5.34) 
    assert str(error.value) == "Please add a task."

"""
when calling present_list, if the list is empty
an error message should come up
"""
def test_empty_list_error_message():
    todo = todo_tasks()
    with pytest.raises(Exception) as N:
        todo.present_tasks() 
    assert str(N.value) == "Todo list is empty. Please add tasks"
    