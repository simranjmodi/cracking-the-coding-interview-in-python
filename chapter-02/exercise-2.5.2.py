"""
2.5 Sum Lists

You have two numbers represented by a linked list, where each node
contains a single digit. The digits are stored in reverse order,
such that the 1's digit is at the head of the list. Write a function
that adds the two numbers and returns the sum as a linked list.

Solution 2: Handles case when one linked list is shorter than
another by padding shorter list with zeroes.
"""

# TO FIX

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#         self.length = 0
#
# class PartialSum:
#     def __init__(self):
#         self.sum = None
#         self.carry = 0
#
# def insert_before(list,data):
#     node = Node(data)
#     if list is not None:
#         node.next = list
#     return node
#
# def pad_list(l, padding):
#     head = l
#     for i in range(padding):
#         head = insert_before(head,0)
#     return head
#
# def add_lists_helper(l1,l2):
#     if l1 is None and l2 is None:
#         sum = PartialSum()
#         return sum
#
#     sum = add_lists_helper(l1.next,l2.next)
#
#     val = sum.carry + l1.data + l2.data
#
#     full_result = insert_before(sum.sum, val%10)
#
#     sum.sum = full_result
#     sum.carry = val%10
#     return sum
#
# def add_lists(l1,l2):
#     len1 = l1.length
#     len2 = l2.length
#
#     if len1 < len2:
#         l1 = pad_list(l1,len2-len1)
#     else:
#         l2 = pad_list(l2,len1-len2)
#
#     sum = add_lists_helper(l1,l2)
#
#     if sum.carry == 0:
#         return sum.sum
#     else:
#         result = insert_before(sum.sum, sum.carry)
#         return result
#
#
