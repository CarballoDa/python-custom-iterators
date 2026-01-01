from custom_iterators import FibonacciIterator

def test_fibonacci_first_values():
    fib = FibonacciIterator()
    assert next(fib) == 0
    assert next(fib) == 1
    assert next(fib) == 1
    assert next(fib) == 2
    assert next(fib) == 3