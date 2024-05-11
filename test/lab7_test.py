import unittest
from src.lab7 import boyer_moore


class TestBoyerMoore(unittest.TestCase):
    def test_empty_needle(self):
        haystack = "abcdefg"
        needle = ""
        self.assertEqual(boyer_moore(haystack, needle), [])

    def test_no_match(self):
        haystack = "abcdefg"
        needle = "xyz"
        self.assertEqual(boyer_moore(haystack, needle), [])

    def test_single_match(self):
        haystack = "abcdefg"
        needle = "cde"
        self.assertEqual(boyer_moore(haystack, needle), [2])


if __name__ == "__main__":
    unittest.main()
