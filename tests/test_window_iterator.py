from custom_iterators import WindowIterator

def test_window_iterator_basic():
    assert list(WindowIterator([1,2,3,4,5], 3)) == [
        [1,2,3],
        [2,3,4],
        [3,4,5]
    ]

def test_window_iterator_no_windows():
    assert list(WindowIterator([1,2], 3)) == []