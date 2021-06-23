"""
4.3 List of Depths

Given a binary tree, design an algorithm which creates a linked list of
all the nodes at each depth (e.g. if you have a tree with depth D, you
will have D linked lists)
"""

from collections import deque

class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def append(self, data):
        current = self.head
        if current is None:
            self.head = Node(data)
            return
        while current.next != None:
            current = current.next

        new_node = Node(data)
        current.next = new_node

    def get(self,index):
        current = self.head
        count = 0

        while current:
            if count == index:
                return current.data
            count += 1
            current = current.next

        return 0


def create_level_linked_list(root: TreeNode):
    queue = deque([root] if root else [])
    ans = LinkedList()

    while len(queue):
        qlen = len(queue)
        row = LinkedList()

        for _ in range(qlen):
            curr = queue.popleft()
            row.append(curr)

            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)

        ans.append(row)
    return ans



