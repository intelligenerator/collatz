import unittest
from collatz import collatz_sequence as collatz


class CollatzTestCase(unittest.TestCase):
    def test_base_case(self):
        base_case = collatz(1)
        self.assertListEqual(base_case, [1])

    def test_3(self):
        sequence = collatz(3)
        self.assertListEqual(sequence, [3, 10, 5, 16, 8, 4, 2, 1])

    def test_5(self):
        sequence = collatz(5)
        self.assertListEqual(sequence, [5, 16, 8, 4, 2, 1])


if __name__ == '__main__':
    unittest.main()
