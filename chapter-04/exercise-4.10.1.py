"""
4.10 Check Subtree

T1 and T2 are very large binary trees, with T1 much bigger than T2. Create an
algorithm to determine if T2 is a subtree of T1

A Tree T2 is a subtree of T1 if there exists a node n in T1 such that the
subtree of n is identical to T2. That is, if you cut off the tree at node n,
the two trees would be identical.

Solution 1: Recursively checking nodes
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def are_identical(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False

    return (root1.data == root2.data and
            are_identical(root1.left, root2.left) and
            are_identical(root1.right, root2.right)
            )

def is_subtree(T, S):
    if S is None:
        return True

    if T is None:
        return False

    if (are_identical(T, S)):
        return True

    return is_subtree(T.left, S) or is_subtree(T.right, S)
