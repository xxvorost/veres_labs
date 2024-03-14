import unittest
from lab2.src.lab2 import longest_sequence


class TestLongestSequence(unittest.TestCase):

    def test_regular_sequence(self):
        self.assertEqual(longest_sequence([1, 2, 3, 4, 5]), 5)

    def test_sequence_with_jokers(self):
        self.assertEqual(longest_sequence([0, 2, 3, 4, 5]), 5)

    def test_sequence_with_more_jokers(self):
        self.assertEqual(longest_sequence([0, 0, 2, 3, 4, 6, 7]), 6)

    def test_sequence_with_duplicates(self):
        self.assertEqual(longest_sequence([1, 2, 2, 3, 4, 5]), 5)

    def test_sequence_with_duplicates_and_jokers(self):
        self.assertEqual(longest_sequence([0, 1, 1, 3, 4, 5, 6]), 6)


if __name__ == '__main__':
    unittest.main()
