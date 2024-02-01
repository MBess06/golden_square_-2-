from lib.string_builder import *

def test_string_builder():
    string_builder = StringBuilder()
    string_builder.add('happy')
    string_builder.size == 5
    result = string_builder.output()
    assert result  == "happy", 5 