"""
Stack space in recursive calls counts too. For example, code like this
would take O(n) time and O(n) space.

Each call adds a level to the stack
1. sum(4)
2.   -> sum(3)
3.        -> sum(2)
4.             -> sum(1)
5.                  -> sum(0)
Each of these calls is added to the call stack and takes up actual memory.
"""


def sum(n):
    if n <= 0:
        return 0
    else:
        return n + sum(n-1)