"""
2.6 Palindrome

Implement a function to check if a linked list is a palindrome

Solution 2: Iterative Approach using Stack
"""

from collections import deque

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def is_palindrome(head):
    fast = head
    slow = head

    stack = deque()

    while fast is not None and fast.next is not None:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next

    if fast is not None:
        slow = slow.next

    while slow is not None:
        top = stack.pop()
        if top != slow.data:
            return False

        slow = slow.next

    return True

