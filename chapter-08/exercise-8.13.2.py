"""
8.13 Stack of Boxes

You have a stack of n boxes, with widths w_i, heights h_i, and depths d_i.
The boxes cannot be rotated and can only be stacked on top of one another
if each box is in the stack is strictly larger than the box above it in
width, height, and depth. Implement a method to compute the height of the
tallest possible stack. The height is the sum of the heights of each box.

Solution 2: Using memoization to cache height of the tallest stack and
making choice at each step whether to put a particular box in the stack.
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
    stack_map = [0] * len(boxes)
    return create_stack_aux(boxes, None, 0, stack_map)

def create_stack_aux(boxes, bottom, offset, stack_map):
    if offset >= len(boxes):
        return 0

    new_bottom = boxes[offset]
    height_with_bottom = 0
    if bottom is None or new_bottom.can_be_above(bottom):
        if stack_map[offset] == 0:
            stack_map[offset] = create_stack_aux(boxes, new_bottom, offset + 1, stack_map)
            stack_map[offset] += new_bottom.h
        height_with_bottom = stack_map[offset]

    height_without_bottom = create_stack_aux(boxes, bottom, offset + 1, stack_map)

    return max(height_with_bottom, height_without_bottom)
