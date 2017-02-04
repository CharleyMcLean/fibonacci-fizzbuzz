import unittest
import fibonacci


class TestCase(unittest.TestCase):
    """Unittest class"""
    def test_find_nth_fibonacci(self):
        """Unittest for finding nth term in Fibonacci series"""
        assert fibonacci.find_nth_fibonacci(4) == 3

    def test_is_prime(self):
        """Unittest for determine if prime or not"""
        assert fibonacci.find_nth_fibonacci(5)

    def test_F(self):
        """Unittest for returned value based on nth term
        of Fibonacci series"""
        assert fibonacci.F(4) == "Buzz"


if __name__ == "__main__":
    unittest.main()
