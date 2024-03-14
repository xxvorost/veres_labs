import unittest
from lab1.src.Labka1 import mono


class Test(unittest.TestCase):
    def test_up(self):
        self.assertTrue(mono([1, 2, 3, 4, 5]))

    def test_down(self):
        self.assertTrue(mono([5, 4, 3, 2, 1]))

    def test_not_mono(self):
        self.assertFalse(mono([1, 2, 2, 3, 2, 4]))
    def test_mono1(self):
     self.assertEqual(mono([2, 2, 2, 2, 2, 3]), True)

    def test_mono2(self):
        self.assertEqual(mono([2, 2, 2, 2, 2, 1]), True)

    def test_mono3(self):
        self.assertEqual(mono([1, 1, 1, 1, 1, 0]), True)





if __name__ == '__main__':
    unittest.main()

