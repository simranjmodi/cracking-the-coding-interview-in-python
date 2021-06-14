"""
2.1 Remove Dups

Write code to remove duplicates from an unsorted linked list

Solution 1: Temporary buffer is allowed
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def remove_duplicates(head):
    if head is None or head.next is None:
        return head

    hash = set()

    current = head
    hash.add(head.data)

    while current.next is not None:
        if current.next.data in hash:
            current.next = current.next.next
        else:
            hash.add(current.next.data)
            current = current.next

    return head


