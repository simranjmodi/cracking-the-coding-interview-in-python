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

def check_BST(n):
    return check_BST_aux(n, None, None)

def check_BST_aux(n, min, max):
    if n is None:
        return True

    if (min is not None and n.data <= min) or (max is not None and n.data > max):
        return False

    if (not check_BST_aux(n.left, min, n.data)) or (not check_BST_aux(n.right, n.data, max)):
        return False

    return True

