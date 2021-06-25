"""
4.8 First Common Ancestor

Design an algorithm and write code to find a first common ancestor of two
nodes in a binary tree. NOTE: This is not necessarily a binary search tree.

Solution 2: Using single traversal
"""

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def find_LCA(root, n1, n2):
    if root is None:
        return None

    if root.key == n1 or root.key == n2:
        return root

    left_lca = find_LCA(root.left, n1, n2)
    right_lca = find_LCA(root.right, n1, n2)

    if left_lca and right_lca:
        return root

    return left_lca if left_lca is not None else right_lca
