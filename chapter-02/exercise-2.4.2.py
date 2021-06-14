"""
2.4 Partition

Write code to partition a linked list around a value x, such that all
nodes less than x come before all nodes greater than or equal to x.
If x is contained within the list, the values of x only need to be after
the elements less than x. The partition element x can appear anywhere
in the "right partition"; it does not need to appear between the left
and right partitions.

Solution 2: Not a "stable" approach
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def partition(node,x):
    head = node
    tail = node

    while node is not None:
        next = node.next
        if node.data < x:
            node.next = head
            head = node
        else:
            tail.next = node
            tail = node
        node = next

    tail.next = None
    return head