from custom_iterators import MapIterator

def test_map_iterator_basic():
    assert list(MapIterator([1,2,3], lambda x: x * 2)) == [2, 4, 6]

def test_map_iterator_identity():
    assert list(MapIterator([1,2,3], lambda x: x)) == [1, 2, 3]