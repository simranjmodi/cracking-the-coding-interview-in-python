"""
12.2 Reverse String

Implement a function to reverse a string
"""

from collections import deque

def reverse(string):
    n = len(string)
    stack = deque()

    for i in range(0, n, 1):
        stack.append((string[i]))

    string = ""
    for i in range(0, n, 1):
        string += stack.pop()

    return string