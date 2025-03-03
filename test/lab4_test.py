import unittest
from src.list_based_priority_queue_lab4 import *


class TestPriorityQueue(unittest.TestCase):
    def test_priority_queue_operations(self):
        pq = PriorityQueue()
        pq.insert('task1', 5)
        pq.insert('task2', 3)
        pq.insert('task3', 8)

        self.assertEqual(pq.peek(), ('task3', 8))
        self.assertEqual(pq.pop(), ('task3', 8))
        self.assertEqual(pq.pop(), ('task1', 5))
        self.assertEqual(pq.pop(), ('task2', 3))
        with self.assertRaises(IndexError):
            pq.pop()


if __name__ == '__main__':
    unittest.main()
