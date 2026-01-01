from custom_iterators import InfiniteEvenNumbers

def test_infinite_even_numbers_first_values():
    it = InfiniteEvenNumbers()
    assert next(it) == 0
    assert next(it) == 2
    assert next(it) == 4