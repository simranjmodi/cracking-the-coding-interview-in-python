"""
2.6 Palindrome

Implement a function to check if a linked list is a palindrome
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def reverse_and_clone(node):
    head = None
    while node is not None:
        n = Node(node.data)
        n.next = head
        head = n
        node = node.next
    return head

def is_equal(one,two):
    while one is not None and two is not None:
        if one.data != two.data:
            return False
        one = one.next
        two = two.next
    return one == None and two == None

def is_palindrome(head):
    reversed = reverse_and_clone(head)
    return is_equal(head,reversed)
