"""
4.12 Paths with Sum

You are given a binary tree in which each node contains an integer value (which
might be positive or negative). Design an algorithm to count the number of paths
that sum to a given value. The path does not need to start or end at the root or
a leaf, but it must go downwards (travelling only from parent nodes to child nodes)

Solution 1: Optimized
"""

class Node:
    def __init__(self, d):
        self.data = d
        self.right = None
        self.left = None

# TODO