"""
3.5 Sort Stack

Write a program to sort a stack such that the smallest items are on the top.
You can use an additional temporary stack, but you may not copy the elements
into any other data structure (such as an array). The stack supports the
following operations: push, pop, peek, and is_empty.
"""

from collections import deque

def sort(stack):
    temp_stack = deque()
    while len(stack) != 0:
        tmp = stack.pop()
        while len(temp_stack) != 0 and temp_stack[-1] > tmp:
            stack.append(temp_stack.pop())

        temp_stack.append(tmp)

    while len(temp_stack) != 0:
        stack.append(temp_stack.pop())
    return stack
