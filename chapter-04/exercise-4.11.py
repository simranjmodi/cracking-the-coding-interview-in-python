"""
4.11 Random Node

You are implementing a binary search tree class from scratch, which, in addition to
insert, find, and delete, has a method get_random_node() which returns a random node
from the tree. All nodes should be equally likely to be chosen. Design and implement
an algorithm for get_random_node(), and explain how you would implement the rest of
the methods.
"""

from random import randint
from random import seed
seed(1)

class TreeNode:
    def __init__(self, d):
        self.data = d
        self.size = 1
        self.right = None
        self.left = None

    def get_size(self):
        return self.size

    def data(self):
        return self.data

    def insert_in_order(self, d):
        if d <= self.data:
            if self.left is None:
                self.left = TreeNode(d)
            else:
                self.left.insert_in_order(d)
        else:
            if self.right is None:
                self.right = TreeNode(d)
            else:
                self.right.insert_in_order(d)
        self.size += 1

    def get_random_node(self):
        left_size = 0 if self.left is None else self.left.size
        index = randint(0,self.size-1)
        if index < left_size:
            return self.left.get_random_node()
        elif index == left_size:
            return self
        else:
            return self.right.get_random_node()

    def find(self, d):
        if d == self.data:
            return self
        elif d <= self.data:
            return self.left.find(d) if self.left is not None else None
        elif d > self.data:
            return self.right.find(d) if self.right is not None else None
        return None

