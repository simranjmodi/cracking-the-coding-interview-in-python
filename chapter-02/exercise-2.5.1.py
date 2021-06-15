"""
2.5 Sum Lists

You have two numbers represented by a linked list, where each node
contains a single digit. The digits are stored in reverse order,
such that the 1's digit is at the head of the list. Write a function
that adds the two numbers and returns the sum as a linked list.

Solution 1: Does not handle condition when one linked list is shorter
than another.
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def add_lists(l1,l2,carry):
    if l1 is None and l2 is None and carry == 0:
        return None
    res = Node(0)
    value = carry
    if l1 is not None:
        value += l1.data
    if l2 is not None:
        value += l2.data
    res.data = value%10
    if l1 is not None or l2 is not None:
        more = add_lists(None if l1 is None else l1.next,
                   None if l2 is None else l2.next,
                   1 if value >= 10 else 0)
        res.next = more
    return res
