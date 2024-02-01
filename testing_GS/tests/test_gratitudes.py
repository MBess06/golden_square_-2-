from lib.gratitudes import *

def test_gratitudes():
    gratitudes = Gratitudes()
    gratitudes.add("family")
    gratitudes.add("food")
    gratitudes.add ("friends")
    result = gratitudes.format()
    assert result == "Be grateful for: family, food, friends"