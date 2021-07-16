"""
10.10 Rank from Stream

Imagine you are reading in a stream of integers. Periodically, you wish
to be able to look up the rank of a number x (the number of values less
than or equal to x). Implement the data structures and algorithms to
support these operations. That is, implement the method track(x), which
is called when each number is generated, and the method get_rank_of_numnber(x),
which returns the number of values less than or equal to x (not including
x itself).
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left, self.right = None, None
        self.leftSize = 0

def insert_node(root, data):
    if root is None:
        return Node(data)

    if data <= root.data:
        root.left = insert_node(root.left, data)
        root.leftSize += 1
    else:
        root.right = insert_node(root.right, data)
    return root

def get_rank(root, x):
    if root.data == x:
        return root.leftSize

    if x < root.data:
        if root.left is None:
            return -1
        else:
            return get_rank(root.left, x)

    else:
        if root.right is None:
            return -1
        else:
            right_size = get_rank(root.right, x)
            if right_size == -1:
                return -1
            else:
                return root.leftSize + 1 + right_size


