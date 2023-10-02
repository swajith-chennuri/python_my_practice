class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    elif value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def preorder_traversal(root):
    if root:
        print(root.value,end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

# Example usage
values =list(map(int,input().split(" ")))

# Build the tree
root = None
for value in values:
    root = insert(root, value)

# Traverse the tree in pre-order and print its elements
preorder_traversal(root)