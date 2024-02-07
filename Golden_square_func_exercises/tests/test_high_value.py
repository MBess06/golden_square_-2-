import pytest
from lib.high_value import *

def test_high_value_start_up():
    highvalue = HighValue(2,5)
    result = [highvalue.value_first, highvalue.value_second]
    assert result == [2,5]
    
def test_higher_first():
    highvalue = HighValue(10, 4)
    result = highvalue.get_highest()
    assert result == "First value is higher"

def test_higher_second():
    highvalue = HighValue(3,7)
    result = highvalue.get_highest()
    assert result == "Second value is higher"

def test_equal():
    highvalue = HighValue(3,3)
    result = highvalue.get_highest()
    assert result == "Values are equal"

def test_add_first():
    highvalue = HighValue(4,4)
    highvalue.add(10, "first")
    result = highvalue.value_first
    assert result == 14

def test_add_second():
    highvalue = HighValue(3,3)
    highvalue.add(5, "second")
    result = highvalue.value_second
    assert result == 8