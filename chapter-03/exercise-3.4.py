"""
3.4 Queue via Stacks

Implement a MyQueue class which implements a queue using two stacks.
"""

from collections import deque

class MyQueue:

    def __init__(self):
        self.stack_newest = deque()
        self.stack_oldest = deque()

    def __len__(self):
        return len(self.stack_newest) + len(self.stack_oldest)

    def add(self, value):
        self.stack_newest.append(value)

    def shift_stacks(self):
        if len(self.stack_oldest) == 0:
            while len(self.stack_newest) != 0:
                self.stack_oldest.append(self.stack_newest.pop())

    def peek(self):
        self.shift_stacks()
        print(self.stack_oldest)
        return self.stack_oldest[-1]

    def remove(self):
        self.shift_stacks()
        self.stack_oldest.pop()
        return
