from custom_iterators import Circular

def test_circular_basic():
    assert list(Circular(["A","B","C"], 5)) == ["A","B","C","A","B"]

def test_circular_zero():
    assert list(Circular([1,2,3], 0)) == []