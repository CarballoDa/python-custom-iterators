from custom_iterators import ReverseList

def test_reverse_list_basic():
    assert list(ReverseList([1, 2, 3])) == [3, 2, 1]

def test_reverse_list_empty():
    assert list(ReverseList([])) == []