from custom_iterators import RestartingIterator

def test_restarting_iterator_basic():
    assert list(RestartingIterator(["A","B","C"], 7)) == ["A","B","C","A","B","C","A"]