"""
2.1 Remove Dups

Write code to remove duplicates from an unsorted linked list
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def remove_duplicates(self,head):
        if self.head is None or self.head.next is None:
            return head

        hash = set()

        current = head
        hash.add(self.head.data)

        while current.next is not None:
            if current.next.data in hash:
                current.next = current.next.next
            else:
                hash.add(current.next.data)
                current = current.next

        return head
