import pytest
from lib.diary_entry import *

"""
Given a title and contnents
format method should return formatted entry- like so; "My Title: These are the contents 
"""
def test_format_with_title_and_contents():
    diary = DiaryEntry("Wednesday seventh January", "Diary Entry Exercise one")
    assert diary.format() == "Wednesday seventh January: Diary Entry Exercise one"

"""
Given a title and a contents
count_words method returns number of words in title and contents 
"""
def test_word_count_with_title_and_contents():
    diary = DiaryEntry("Wednesday seventh January", "Diary Entry Exercise one")
    assert diary.count_words() == 7

"""
Given an empty title or contents
raise an error
"""
def test_empty_title_and_contents():
    with pytest.raises(Exception) as e:
        DiaryEntry("","")
    assert str(e.value) == "Diary entry must have title or contents"

"""
Given a contents and a wpm of 2
reading time method should return estimated words per minute =>
"""
def test_reading_time_4_mins_4_words():
    diary = DiaryEntry("Wednesday seventh January", "Diary Entry Exercise one two three four five")
    assert diary.reading_time(2) == 4

"""
Given a content of 2 words and and wpm of 1
reading time method should return 2
"""

def test_reading_time_1_mins_2_words():
    diary = DiaryEntry("Wednesday seventh January", "Diary Entry")
    assert diary.reading_time(1) == 2

"""
Given a content of 5 words and and wpm of 2
reading time method should return 3
"""
def test_reading_time_2_mins_5_words():
    diary = DiaryEntry("Wednesday seventh January", "Diary Entry excercise one two")
    assert diary.reading_time(2) == 3

"""
Given a wpm of 0
reading time method should raise error message
"""
def test_reading_time_0_wpm():
    diary = DiaryEntry("Wednesday seventh January", "Diary Entry")
    with pytest.raises(Exception) as err:
        diary.reading_time(0)
    assert str(err.value) == "Can read this under a minute"

"""
Given an empty title or contents
raise an error
"""
def test_empty_title():
    with pytest.raises(Exception) as e:
        DiaryEntry("","contents")
    assert str(e.value) == "Diary entry must have title or contents"

"""
Given an empty title or contents
raise an error
"""
def test_empty_contents():
    with pytest.raises(Exception) as e:
        DiaryEntry("title","")
    assert str(e.value) == "Diary entry must have title or contents"

"""
Given a content of 8 words 
wpm of 2
and mins of 4
reading chunk method should return the first 4 words
"""
def test_reading_chunk_with_2_wpm_and_4_mins():
    diary = DiaryEntry("Diary Title", "How long will this text take to read? I think six minutes")
    assert diary.reading_chunk(2,4) == "How long will this text take to read?"

"""
Given a content of 8 words 
wpm of 2
and mins of 1
reading chunk method should return the first 2 words
"""
def test_reading_chunk_with_2_wpm_and_1_mins():
    diary = DiaryEntry("Diary Title", "How long will this text take to read? I think six minutes")
    assert diary.reading_chunk(2,1) == "How long"

"""
Given a content of 8 words 
wpm of 2
and mins of 1
reading chunk method should return the first 2 words
Then when reading chunk method is called again, next 2 words will return
"""
def test_reading_chunk_twice_called():
    diary = DiaryEntry("Diary Title", "How long will this text take to read? I think six minutes")
    assert diary.reading_chunk(2,1) == "How long"
    assert diary.reading_chunk(2,1) == "will this"

"""
Given a content of 8 words 
wpm of 2
and mins of 1
reading chunk method should return the first 2 words
Then when reading chunk method is called again, next 2 words will return
"""
def test_reading_chunk_trice_called():
    diary = DiaryEntry("Diary Title", "How long will this text take to read? I think six minutes")
    assert diary.reading_chunk(2,1) == "How long"
    assert diary.reading_chunk(1,1) == "will"
    assert diary.reading_chunk(2,1) == "this text"

"""
Given a content of 12 words, wpm is 2, minutes 2
when contents fully read 
the next call should restart from the beginning of the contents
"""
def test_reading_chunk_restarts():
    diary = DiaryEntry("Diary Title", "How long will this text take to read? I think six minutes")
    assert diary.reading_chunk(2,2) == "How long will this"
    assert diary.reading_chunk(2,2) == "text take to read?"
    assert diary.reading_chunk(2,2) == "I think six minutes"
    assert diary.reading_chunk(2,2) == "How long will this"