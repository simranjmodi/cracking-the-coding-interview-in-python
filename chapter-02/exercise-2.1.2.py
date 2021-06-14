"""
2.1 Remove Dups

Write code to remove duplicates from an unsorted linked list

Solution 2: Temporary buffer is not allowed
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def remove_duplicates(head):
    current = head
    while current is not None:
        runner = current
        while runner.next is not None:
            if runner.next.data == current.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next



