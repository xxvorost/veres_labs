import unittest
from VERESlabs.src.lab3 import post_order_traversal, BinaryTree


class TestTree(unittest.TestCase):
    def test_tree(self):
        root = BinaryTree(3)
        root.left = BinaryTree(9)
        root.right = BinaryTree(20)

        self.assertEqual(post_order_traversal(root), [9, 20, 3])


if __name__ == '__main__':
    unittest.main()
