"""
2.7 Intersection

Given two (singly) linked lists, determine if the two lists intersect.
Return the intersection node. Note that the intersection is defined
based on reference, not value. That is, if the kth node of the first
linked list is the exact same node (by reference) as the jth node of
second linked list, then they are intersecting.
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def get_intersection_node(list1, list2):
    l1 = list1
    l2 = list2

    while l1 != l2:
        l1 = list2 if l1 is None else l1.next
        l2 = list1 if l2 is None else l2.next
    return l1

