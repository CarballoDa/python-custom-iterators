from custom_iterators import StepIterator

def test_step_iterator_basic():
    assert list(StepIterator([1,2,3,4,5,6], 2)) == [1, 3, 5]

def test_step_iterator_step_one():
    assert list(StepIterator([10,20,30], 1)) == [10, 20, 30]