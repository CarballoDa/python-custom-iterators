from custom_iterators import SimpleCounter

def test_simple_counter_basic():
    assert list(SimpleCounter(3)) == [0, 1, 2, 3]

def test_simple_counter_zero():
    assert list(SimpleCounter(0)) == [0]