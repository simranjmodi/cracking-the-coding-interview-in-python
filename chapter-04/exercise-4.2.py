"""
4.2 Minimal Tree

Given a sorted (increasing order) array with unique integer elements, write
an algorithm to create a binary search tree with minimal height.
"""

class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

def sorted_array_to_BST(arr):
    if not arr:
        return None

    mid = (len(arr)) // 2
    root = Node(arr[mid])

    root.left = sorted_array_to_BST(arr[:mid])
    root.right = sorted_array_to_BST(arr[mid + 1:])

    return root

