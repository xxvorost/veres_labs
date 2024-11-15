import unittest

from src.lab5 import read_input, bfs_shortest_path


class TestLab5(unittest.TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.input_path = None

    def test_read_input(self):
        start, end, grid = read_input(self.input_path)
        self.assertEqual(start, (0, 0))
        self.assertEqual(end, (3, 3))
        self.assertEqual(grid, [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 0, 1],
            [0, 0, 1, 1, 1],
            [1, 1, 1, 1, 1]
        ])

    def test_bfs_shortest_path_correct(self):
        grid = [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 0, 1],
            [0, 0, 1, 1, 1],
            [1, 1, 1, 1, 1]
        ]
        start = (0, 0)
        end = (3, 3)
        result = bfs_shortest_path(grid, start, end)
        self.assertEqual(result, 6)


if __name__ == "__main__":
    unittest.main()
