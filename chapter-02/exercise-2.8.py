"""
2.8 Loop Detection

Given a circular linked list, implement an algorithm that returns the
node at the beginning of the loop
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def detect_loop(head):
    sp = head
    fp = head
    while (sp and fp and fp.next):
        sp = sp.next
        fp = fp.next.next
        if sp == fp:
            return True
    return False