class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def tree_sum(root):
    if root is None:
        return 0
    return root.value + tree_sum(root.left) + tree_sum(root.right)

# Приклад використання:
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(8)
root.right.left = TreeNode(12)
root.right.right = TreeNode(20)
print("Сума всіх значень у дереві:", tree_sum(root))
