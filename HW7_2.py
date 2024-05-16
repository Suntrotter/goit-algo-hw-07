class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

def find_min_value(root):
    current = root
    while current.left:
        current = current.left
    return current.value

def height(node):
    if not node:
        return 0
    return node.height

def update_height(node):
    node.height = 1 + max(height(node.left), height(node.right))

def balance_factor(node):
    if not node:
        return 0
    return height(node.left) - height(node.right)

def rotate_right(y):
    x = y.left
    T2 = x.right
    
    # Perform rotation
    x.right = y
    y.left = T2
    
    # Update heights
    update_height(y)
    update_height(x)
    
    return x

def insert(root, value):
    if not root:
        return TreeNode(value)
    
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    
    update_height(root)
    
    balance = balance_factor(root)
    
    # Rebalance the tree if necessary
    if balance > 1:
        if value < root.left.value:
            return rotate_right(root)
    return root

# Example usage:
root = None
root = insert(root, 10)
root = insert(root, 5)
root = insert(root, 15)
root = insert(root, 3)
root = insert(root, 8)
root = insert(root, 12)
root = insert(root, 20)
print(find_min_value(root))
