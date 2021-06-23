"""
4.3 List of Depths

Given a binary tree, design an algorithm which creates a linked list of
all the nodes at each depth (e.g. if you have a tree with depth D, you
will have D linked lists)
"""


# TO FIX


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

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

def create_level_linked_list(root, lists, level):
    if root is None:
        return

    list = None
    if lists.size() == level:
        list = LinkedList()
        lists.append(list)
    else:
        list = lists.get(level)

    list.append(root)
    create_level_linked_list(root.left, lists, level+1)
    create_level_linked_list(root.right, lists, level+1)

def main(root):
    lists = LinkedList()
    create_level_linked_list(root, lists, 0)
    return lists

""" 
        4
    2       3
  5   6   7    8


"""

root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(6)
root.right = TreeNode(3)
root.right.left = TreeNode(7)
root.right.right = TreeNode(8)

lst = main(root)

