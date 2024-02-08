import pytest
from lib.mark_tasks import *

"""
when presenting incomplete tasks- the list should be empty
"""
def test_empty_incompleted_list():
    mark = mark_tasks()
    assert mark.incomplete_tasks() == []

"""
When we add a task it is reflected in the incompleted taks list
"""
def test_add_one_task_todo():
    mark = mark_tasks()
    mark.add_task("Feed the cat.")
    assert mark.incomplete_tasks() == ["Feed the cat."]

"""
When adding multiple tasks it is added to list
and refelct in incompleted meth
"""
def test_adding_another_tasks():
    mark = mark_tasks()
    mark.add_task("Feed the cat.")
    mark.add_task("Feed the fish.")
    assert mark.incomplete_tasks() == ["Feed the cat.","Feed the fish."]

def test_adding_multiple_tasks():
    mark = mark_tasks()
    mark.add_task("Feed the cat.")
    mark.add_task("Feed the fish.")
    mark.add_task("Feed the lion.")
    assert mark.incomplete_tasks() == ["Feed the cat.","Feed the fish.","Feed the lion."]

"""
When indexing a num in the completed tasks method
It removes that indexed task from the list
"""
def test_mark_index_1_in_tasks():
    mark = mark_tasks()
    mark.add_task("Feed the cat.")
    mark.add_task("Feed the fish.")
    mark.add_task("Feed the lion.")
    mark.complete_tasks(1)
    assert mark.incomplete_tasks() == ["Feed the cat.","Feed the lion."]

"""
If we try to to mark a task out of the range of the list (too low)
error message will be shown
"""
def test_index_too_low():
    mark = mark_tasks()
    mark.add_task("Feed the cat.")
    mark.add_task("Feed the fish.")
    mark.add_task("Feed the lion.")
    with pytest.raises(Exception) as e:
        mark.complete_tasks(-3)
    assert str(e.value) == "Out of list range"
    assert mark.incomplete_tasks() == ["Feed the cat.","Feed the fish.","Feed the lion."]

"""
If we try to to mark a task out of the range of the list (too high)
error message will be shown
"""
def test_index_too_high():
    mark = mark_tasks()
    mark.add_task("Feed the cat.")
    mark.add_task("Feed the fish.")
    mark.add_task("Feed the lion.")
    with pytest.raises(Exception) as e:
        mark.complete_tasks(6)
    assert str(e.value) == "Out of list range"
    assert mark.incomplete_tasks() == ["Feed the cat.","Feed the fish.","Feed the lion."]

