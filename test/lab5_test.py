import unittest
import os
from src.lab5 import *


# Вставте тут код вашої програми, замість `main()` використовуйте функції безпосередньо у тестах

def write_input(file_path, start, end, grid):
    with open(file_path, 'w') as file:
        file.write(','.join(map(str, start)) + '\n')
        file.write(','.join(map(str, end)) + '\n')
        file.write(','.join(map(str, (len(grid), len(grid[0])))) + '\n')
        for row in grid:
            file.write('[' + ' '.join(map(str, row)) + ']\n')


def read_output(file_path):
    with open(file_path, 'r') as file:
        return int(file.readline().strip())


class TestBFSPathFinding(unittest.TestCase):
    def setUp(self):
        self.input_file = "test_input.txt"
        self.output_file = "test_output.txt"

    def test_bfs_path_found(self):
        start = (0, 0)
        end = (2, 2)
        grid = [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]
        expected_output = 4
        write_input(self.input_file, start, end, grid)
        start, end, grid = read_input(self.input_file)
        result = bfs_shortest_path(grid, start, end)
        write_output(self.output_file, result)
        self.assertEqual(read_output(self.output_file), expected_output)

    def test_bfs_no_path(self):
        start = (0, 0)
        end = (2, 2)
        grid = [
            [1, 0, 1],
            [0, 0, 1],
            [1, 1, 1]
        ]
        expected_output = -1
        write_input(self.input_file, start, end, grid)
        start, end, grid = read_input(self.input_file)
        result = bfs_shortest_path(grid, start, end)
        write_output(self.output_file, result)
        self.assertEqual(read_output(self.output_file), expected_output)

    def tearDown(self):
        os.remove(self.input_file)
        os.remove(self.output_file)


if __name__ == '__main__':
    unittest.main()
