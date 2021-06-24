"""
4.6 Successor

Write an algorithm to find the "next" node (i.e in-order sequence) of a
given node in a binary search tree. You may assume that each node has
a link to its parent.
"""

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def insert(node, data):
    if node is None:
        return Node(data)
    else:
        if data <= node.data:
            temp = insert(node.left, data)
            node.left = temp
            temp.parent = node
        else:
            temp = insert(node.right, data)
            node.right = temp
            temp.parent = node
        return node

def in_order_succ(n):
    if n is None:
        return None

    if n.right is not None:
        return left_most_child(n.right)
    else:
        q = n
        x = q.parent

        while x is not None and x.left is not q:
            q = x
            x = x.parent

        return x

def left_most_child(n):
    if n is None:
        return None
    while n.left is not None:
        n = n.left
    return n

