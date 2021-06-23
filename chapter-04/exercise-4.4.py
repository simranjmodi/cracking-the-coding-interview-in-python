"""
4.4 Check Balanced

Implement a function to check if a binary tree is balanced. For the purposes
of this question, a balanced tree is defined to be a tree such that the
heights of the two subtrees of any node never differ by more than one.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def check_height(root):
    if root is None:
        return -1

    left_height = check_height(root.left)
    if left_height == -2:
        return -2

    right_height = check_height(root.right)
    if right_height == -2:
        return -2
    height_diff = left_height - right_height
    if abs(height_diff) > 1:
        return -2
    else:
        return max(left_height,right_height) + 1

def is_balanced(root):
    return check_height(root) != -2