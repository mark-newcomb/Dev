from src.main.python.main_dev import add_nums


def test_add_nums():
    assert add_nums(1, 2) == 3

def func(a):
    return a**2

def test_func():
    assert func(2) == 4

# Use pytest -vv for verbose reporting
# Use pytest -k <string> -v for running specific tests
