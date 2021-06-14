"""
2.2 Return Kth to Last

Implement an algorithm to find the kth to last element of a single
linked list

Solution 2: Iterative and optimal
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def nth_to_last(head,k):
    p1 = head
    p2 = head

    for i in range(k):
        if p1 is None:
            return None
        p1 = p1.next

    while p1 is not None:
        p1 = p1.next
        p2 = p2.next

    return p2