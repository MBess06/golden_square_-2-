
from lib.counter import Counter

# returns number given/ adds num to counter(0)

def test_counter_adds_given_num_to_count():
    counter = Counter()
    counter.add(5)
    result = counter.report()
    assert result == "Counted to 5 so far."
