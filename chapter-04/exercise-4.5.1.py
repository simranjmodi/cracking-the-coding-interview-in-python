"""
4.5 Validate BST

Implement a function to check if a binary tree is a binary search tree

Solution 1: In Order Traversal (Assuming no duplicate elements)
"""

last_printed = None

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def check_BST(n):
    global last_printed

    if n == None:
        return True

    if not check_BST(n.left):
        return False

    if last_printed is not None and n.data <= last_printed:
        return False

    last_printed = n.data

    if not check_BST(n.right):
        return False

    return True



