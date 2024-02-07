from grammar_user import *

"""
Given a string which has a capital letter at the start and a punctuation mark at the end.
Returns true
"""
def test_grammar_is_valid_with_Q():
    assert check_grammar("What time is it?") == True

def test_grammar_is_valid_with_full_stop():
    assert check_grammar("It is raining outside.") == True

def test_grammar_is_valid_with_exclaim():
    assert check_grammar("What a beautiful day!") == True

"""
Given a string where the first letter is lower case but has a punctuation mark at the end 
Returns false 
"""
def test_grammar_invalid_no_capital():
    assert check_grammar("i added sugar to my coffee.") == False

"""
Given a string where the ending does not have a punctuation mark but has a capital letter
Returns false
"""
def test_grammar_invalid_no_punc_mark():
    assert check_grammar("Did my package come") == False

"""
Given an empty string or any other data type 
Return "No text provided."
"""
def test_grammar_wrong_data_type():
    assert check_grammar(37478) == "No text provided."

def test_grammar_empty_arg():
    assert check_grammar("") == "No text provided."