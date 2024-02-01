import pytest
from lib.password_checker import *

def test_password_checker_returns_true():
    passwordCheck = PasswordChecker()
    result = passwordCheck.check("QWerty123")
    assert result == True

def test_password_checker_error_for_invalid():
    passwordCheck = PasswordChecker()
    with pytest.raises(Exception) as e:
        passwordCheck.check("Qwerty")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."