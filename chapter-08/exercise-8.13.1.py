"""
8.13 Stack of Boxes

You have a stack of n boxes, with widths w_i, heights h_i, and depths d_i.
The boxes cannot be rotated and can only be stacked on top of one another
if each box is in the stack is strictly larger than the box above it in
width, height, and depth. Implement a method to compute the height of the
tallest possible stack. The height is the sum of the heights of each box.

Solution 1: Recursive solution with memoization
"""

class Box:
    def __init__(self, h, w, d):
        self.h = h
        self.w = w
        self.d = d

    def __lt__(self, other):
        return self.d * self.w < other.d * other.w

    def can_be_above(self, box):
        return (box.h < self.h) and (box.w < self.w) and (box.d < self.d)

def create_stack(boxes):
    boxes = sorted(boxes)
    max_height = 0
    stack_map = [0] * len(boxes)
    for i in range(len(boxes)):
        height = create_stack_aux(boxes, i, stack_map)
        max_height = max(max_height, height)
    return max_height

def create_stack_aux(boxes, bottom_index, stack_map):
    if bottom_index < len(boxes) and stack_map[bottom_index] > 0:
        return stack_map[bottom_index]

    bottom = boxes[bottom_index]
    max_height = 0
    for i in range(bottom_index+1,len(boxes)):
        if boxes[i].can_be_above(bottom):
            height = create_stack_aux(boxes, i, stack_map)
            max_height = max(height, max_height)

    max_height += bottom.h
    stack_map[bottom_index] = max_height
    return max_height
