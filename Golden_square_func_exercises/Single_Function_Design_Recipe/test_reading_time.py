import pytest
from reading_time import *

"""
test function takes integer as an argument 
test function divides argument by 200
test function rounds the result to an integer
test function returns string of '_ minutes'
test for errors when given an empty string 
"""

def test_reading_time_for_4560():
    read_time = reading_time(4560)
    assert read_time == "It will take 23 minutes to read this text"

def test_reading_time_for_2000():
    read_time = reading_time(2000)
    assert read_time == "It will take 10 minutes to read this text"

def test_reading_time_for_empty_arg():
    with pytest.raises(Exception) as e:
        reading_time(None)
    error_message = str(e.value)
    assert error_message == "No text length given. 0 minutes"

