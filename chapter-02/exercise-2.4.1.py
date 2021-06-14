"""
2.4 Partition

Write code to partition a linked list around a value x, such that all
nodes less than x come before all nodes greater than or equal to x.
If x is contained within the list, the values of x only need to be after
the elements less than x. The partition element x can appear anywhere
in the "right partition"; it does not need to appear between the left
and right partitions.

Solution 1: "Stable" approach where elements stay in original order
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def partition(node,x):
    before_start = None
    before_end = None
    after_start = None
    after_end = None

    while node is not None:
        next = node.next
        node.next = None
        if node.data < x:
            if before_start is None:
                before_start = node
                before_end = before_start
            else:
                before_end.next = node
                before_end = node
        else:
            if after_start is None:
                after_start = node
                after_end = after_start
            else:
                after_end.next = node
                after_end = node
        node = next

    if before_start is None:
        return after_start

    before_end.next = after_start
    return before_start
