from lib.count_words import *
#takes string as argument 
#returns number of words in the string 

def test_string_is_split():
    count = CountWords("I need to buy a suitcase, my flight is next week!")
    assert count == 11

def test_num_words_in_string():
    count = CountWords("This should return 10 words unless I have counted wrong")
    assert count == 10