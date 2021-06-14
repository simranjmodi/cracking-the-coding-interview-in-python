"""
2.2 Return Kth to Last

Implement an algorithm to find the kth to last element of a single
linked list

Solution 1: Recursive + Not returning the element
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def print_kth_to_last(head,k):
    if head is None:
        return 0
    index = print_kth_to_last(head.next,k) + 1
    if index == k:
        print("{}th to last node is {}".format(k,head.data))
    return index