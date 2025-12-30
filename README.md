# Python Custom Iterators

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Status](https://img.shields.io/badge/status-active-success)
![Tests](https://img.shields.io/badge/tests-doctest-informational)

A collection of educational Python iterator classes, each demonstrating a different iteration pattern, stateful behavior, or functional transformation.

This project is designed as a learning resource for mastering:

- `__iter__()` and `__next__()`
- Stateful and infinite iterators  
- Functional-style iteration  
- Sliding windows  
- Circular iteration  
- Iterator composition and transformation  

All classes include:

- Clean and readable implementations  
- English docstrings  
- Doctests for validation  
- Usage examples  

---

## Installation

Install the package locally:

```bash
pip install .
```

Or install in editable mode (recommended for development):

```bash
pip install -e .
```

## Usage Example

```bash
from custom_iterators import SimpleCounter, Circular, FibonacciIterator

print(list(SimpleCounter(5)))
# [0, 1, 2, 3, 4, 5]

print(list(Circular(["A", "B", "C"], 7)))
# ['A', 'B', 'C', 'A', 'B', 'C', 'A']

fib = FibonacciIterator()
print(next(fib))  # 0
print(next(fib))  # 1
print(next(fib))  # 1
```

## Project Structure

python-custom-iterators/
│
├── custom_iterators/
│   ├── __init__.py
│   ├── iterators.py
│
├── tests/
├── README.md
├── pyproject.toml
└── LICENSE

## Running Doctest

```bash
python -m pytest --doctest-glob="*.py"
```

Or using Python’s built‑in doctest module:

```bash
python -m doctest -v custom_iterators/iterators.py
```

## License

This project is released under the MIT License.

## Contributing

Contributions, improvements, and new iterator ideas are welcome.
Feel free to open issues or submit pull requests.
