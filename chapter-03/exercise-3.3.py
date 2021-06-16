"""
3.3 Stack of Plates

Implement a data structure SetOfStacks which should be composed
of several stacks and should create a new stack once the previous
one exceeds the capacity. SetOfStacks.push() and SetOfStacks.pop()
should behave identically to a single stack.
"""

from collections import deque

class SetOfStacks:
    def __init__(self):
        self.stacks = []

    def get_last_stack(self):
        if len(self.stacks) == 0:
            return None
        else:
            return self.stacks[-1]

    def push(self,v):
        last = self.get_last_stack()
        if last is not None and not last.is_full():
            last.push(v)
        else:
            stack = deque()
            stack.append(v)
            self.stacks.append(stack)

    def pop(self):
        last = self.get_last_stack()
        if last is None:
            return Exception
        v = last.pop()
        if last.size == 0:
            self.stacks.pop(len(self.stacks)-1)
        return v