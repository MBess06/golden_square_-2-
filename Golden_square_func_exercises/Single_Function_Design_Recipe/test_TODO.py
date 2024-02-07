import pytest
from TODO import *
"""
Given an empity string 
Return False
"""
def test_empty_string():
    result = check_TODO_list("")
    assert result == False

"""
Given a string contains #TODO 
Return True
"""

def test_string_contains_TODO():
    result = check_TODO_list("#TODO")
    assert result == True

"""
Given a string containing #TODO and other characters 
Returns True
"""
def test_string_contains_TODO_and_other_chars():
    result = check_TODO_list("cbdyhf #TODO vhbuvf")
    assert result == True