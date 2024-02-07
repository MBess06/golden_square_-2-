from lib.exercise2 import *

def test_encode():
    assert encode("theswiftfoxjumpedoverthelazydog", "secretkey") == "EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL"

def test_encode_more():
    assert encode("letsseewhatthiswillencode", "secretkey") == "PBEAABBXMHEEMNAXNPPBRCSJB"



def test_decode_1():
    assert decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey") == "theswiftfoxjumpedoverthelazydog"

def test_decode_2():
    assert decode("PBEAABBXMHEEMNAXNPPBRCSJB", "secretkey") == "letsseewhatthiswillencode"





