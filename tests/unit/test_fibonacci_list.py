from __future__ import annotations
from unittest import TestCase, main

from fibonacci.fibonacci.collection import FibonacciLinear


class GetItem(TestCase):
    def test_1st_equals_to_0(self):
        fibonacci = FibonacciLinear()
        self.assertEqual(fibonacci[0], 0)

    def test_2nd_equals_to_1(self):
        fibonacci = FibonacciLinear()
        self.assertEqual(fibonacci[1], 1)

    def test_5th_equals_to_3(self):
        fibonacci = FibonacciLinear()
        self.assertEqual(fibonacci[4], 3)

    def test_10th_equals_to_34(self):
        fibonacci = FibonacciLinear()
        self.assertEqual(fibonacci[9], 34)

if __name__ == "__main__":
    main()
