"""
4.10 Check Subtree

T1 and T2 are very large binary trees, with T1 much bigger than T2. Create an
algorithm to determine if T2 is a subtree of T1

A Tree T2 is a subtree of T1 if there exists a node n in T1 such that the
subtree of n is identical to T2. That is, if you cut off the tree at node n,
the two trees would be identical.

Solution 2: Saving pre-order traversal in a string
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def get_order_string(node, sb):
    if node is None:
        sb += "X"
        return

    sb += (str(node.data) + " ")
    get_order_string(node.left, sb)
    get_order_string(node.right, sb)

def contains_tree(t1, t2):
    str1, str2 = "", ""
    get_order_string(t1, str1)
    get_order_string(t2, str2)
    return str2 in str1

