"""
2.3 Delete Middle Node

Implement an algorithm to delete a node in the middle (i.e any node
but the first and last node, not necessarily the exact middle)
of a single linked list, given only access to that node.
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def delete_node(n):
    if n is None or n.next is None:
        return False

    next = n.next
    n.data = next.data
    n.next = next.next
    return True

