import unittest
import os


def write_input(levels):
    with open("career.in", "w") as file:
        file.write(f"{len(levels)}\n")
        for level in levels:
            file.write(" ".join(map(str, level)) + "\n")


def read_output():
    with open("career.out", "r") as file:
        return int(file.readline().strip())


def calculate_max_experience():
    with open("career.in", "r") as file:
        L = int(file.readline().strip())
        levels = []
        for _ in range(L):
            level = list(map(int, file.readline().strip().split()))
            levels.append(level)
    for i in range(len(levels) - 2, -1, -1):
        for j in range(len(levels[i])):
            levels[i][j] += max(levels[i + 1][j], levels[i + 1][j + 1])
    with open("career.out", "w") as file:
        file.write(str(levels[0][0]))


class TestCareerMaxExperience(unittest.TestCase):
    def test_example1(self):
        levels = [
            [4],
            [3, 1],
            [2, 1, 5],
            [1, 3, 2, 1]
        ]
        expected_output = 12
        write_input(levels)
        calculate_max_experience()
        self.assertEqual(read_output(), expected_output)

    def test_example2(self):
        levels = [
            [9999]
        ]
        expected_output = 9999
        write_input(levels)
        calculate_max_experience()
        self.assertEqual(read_output(), expected_output)

    def test_example3(self):
        levels = [
            [0],
            [1, 1],
            [0, 0, 0],
            [1, 1, 1, 1],
            [0, 1, 0, 1, 0]
        ]
        expected_output = 3
        write_input(levels)
        calculate_max_experience()
        self.assertEqual(read_output(), expected_output)

    def tearDown(self):
        os.remove("career.in")
        os.remove("career.out")


if __name__ == '__main__':
    unittest.main()
