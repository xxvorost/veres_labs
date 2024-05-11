class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def post_order_traversal(root: BinaryTree) -> list:
    if root is None:
        return []

    left_value = post_order_traversal(root.left)
    right_value = post_order_traversal(root.right)

    return left_value + right_value + [root.value]
