"""
4.8 First Common Ancestor

Design an algorithm and write code to find a first common ancestor of two
nodes in a binary tree. NOTE: This is not necessarily a binary search tree.

Solution 1: By Storing root to n1 and root to n2 paths
"""

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def find_path(root, path, k):
    if root is None:
        return False

    path.append(root.key)

    if root.key == k:
        return True

    if ((root.left != None and find_path(root.left, path, k)) or
            (root.right != None and find_path(root.right, path, k))):
        return True

    path.pop()
    return False

def find_LCA(root, n1, n2):
    path1 = []
    path2 = []

    if (not find_path(root, path1, n1) or not find_path(root, path2, n2)):
        return -1

    i = 0
    while (i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i - 1]

