import unittest
from src.list_based_priority_queue_lab4 import PriorityQueue


class TestPriorityQueue(unittest.TestCase):

    def test_insert_and_peek(self):
        pq = PriorityQueue()
        pq.insert('task1', 5)
        pq.insert('task2', 3)
        pq.insert('task3', 8)

        self.assertEqual(pq.peek(), ('task3', 8))

    def test_pop_correct_order(self):
        pq = PriorityQueue()
        pq.insert('task1', 5)
        pq.insert('task2', 3)
        pq.insert('task3', 8)

        self.assertEqual(pq.pop(), ('task3', 8))
        self.assertEqual(pq.pop(), ('task1', 5))
        self.assertEqual(pq.pop(), ('task2', 3))

    def test_insert_with_same_priority(self):
        pq = PriorityQueue()
        pq.insert('task1', 5)
        pq.insert('task2', 5)
        pq.insert('task3', 5)

        self.assertEqual(pq.pop(), ('task1', 5))
        self.assertEqual(pq.pop(), ('task2', 5))
        self.assertEqual(pq.pop(), ('task3', 5))


if __name__ == "__main__":
    unittest.main()
