"""
4.12 Paths with Sum

You are given a binary tree in which each node contains an integer value (which
might be positive or negative). Design an algorithm to count the number of paths
that sum to a given value. The path does not need to start or end at the root or
a leaf, but it must go downwards (travelling only from parent nodes to child nodes)

Solution 1: Brute Force
"""

class Node:
    def __init__(self, d):
        self.data = d
        self.right = None
        self.left = None

def count_paths_with_sum_from_node(node, target_sum, current_sum):
    if node is None:
        return 0

    current_sum += node.data

    total_paths = 0
    if current_sum == target_sum:
        total_paths += 1

    total_paths += count_paths_with_sum_from_node(node.left, target_sum, current_sum)
    total_paths += count_paths_with_sum_from_node(node.right, target_sum, current_sum)
    return total_paths


def count_paths_with_sum(root, target_sum):
    if root is None:
        return 0

    paths_from_root = count_paths_with_sum_from_node(root, target_sum, 0)

    paths_on_left = count_paths_with_sum(root.left, target_sum)
    paths_on_right = count_paths_with_sum(root.right, target_sum)

    return paths_from_root + paths_on_left + paths_on_right
