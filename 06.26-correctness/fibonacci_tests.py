import unittest
import fibonacci as fib


class TestFibonacci(unittest.TestCase):
    def test01(self):
        self.assertEqual(fib.fibonacci(0), 0)

    # If all we have is the above test, the trivial function that simply
    #  always returns 0 would pass all of our tests.

    def test02(self):
        self.assertEqual(fib.fibonacci(1), 1)

    # If all we had were the above two tests, we would not have 100% coverage;
    #  we would never have tested the recursive case.

    def test03(self):
        self.assertEqual(fib.fibonacci(4), 3)

    # Note that even with 100% coverage, we can only be reasonably confident
    #  in the code we wrote. Coverage cannot tell us if we needed to write more
    #  code. For example, if we wanted to handle negative values, the code we
    #  wrote is covered and correct, but we would need a fourth case:

    # def test04(self):
    #    self.assertIsNone(fib.fibonacci(-1))


if __name__ == "__main__":
    unittest.main()
