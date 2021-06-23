"""
4.5 Validate BST

Implement a function to check if a binary tree is a binary search tree

Solution 2: Min/Max Solution using min and max values for progressively
narrower ranges as iterating through the tree.
"""

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
"""
        4
    2       5
 1     3
"""
if (check_BST(root)):
    print("Is BST")
else:
    print("Not a BST")
