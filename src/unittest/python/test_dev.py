from src.main.python.main_dev import add_nums
from src.main.python.main_dev import main

class TestDev:
    @staticmethod
    def func(a):
        return a**2

    def test_func(self):
        assert self.func(2) == 4

class TestMain:
    def test_add_nums(self):
        assert add_nums(1, 2) == 3

    def test_main(self):
        assert main() == 0

# Use pytest -vv for verbose reporting
# Use pytest -k <string> -v for running specific unittest
