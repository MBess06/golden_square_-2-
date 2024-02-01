import pytest
from lib.present import *

def test_present__return_wrap_contents():
    present = Present()
    present.wrap(66)
    assert present.unwrap() == 66

def test_errors_in_present_unwrapped():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

def test_errors_in_wrapped():
    present = Present()
    present.wrap(34)
    with pytest.raises(Exception) as e:
        present.wrap(55)
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."