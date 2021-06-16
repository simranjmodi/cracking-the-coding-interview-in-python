"""
3.2 Stack Min

How would you design a stack which, in addition to push and pop,
has a function min which returns the minimum element? Push, pop
and min should all operate in O(1) time
"""

from collections import deque

class MinStack:
    def __init__(self):
        self.s = deque()
        self.aux = deque()

    def push(self, x):
        self.s.append(x)

        if not self.aux:
            self.aux.append(x)
        else:
            if self.aux[-1] >= x:
                self.aux.append(x)

    def pop(self):
        if self.empty():
            print("Stack underflow")
            return -1

        top = self.s.pop()
        if top == self.aux[-1]:
            self.aux.pop()

        return top

    def peek(self):
        return self.s[-1]

    def empty(self):
        return not self.s

    def min(self):
        if not self.aux:
            print("Stack underflow")
            return -1
        return self.aux[-1]

