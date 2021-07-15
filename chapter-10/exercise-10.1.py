"""
10.1 Sorted Merge

You are given two sorted arrays, A and B, where A has a large enough buffer
at the end to hold B. Write a method to merge B into A in sorted order.
"""

def merge(a, b, last_a, last_b):
    index_a = last_a - 1
    index_b = last_b - 1
    index_merged = last_b + last_a - 1

    while index_b >= 0:
        if index_a >= 0 and a[index_a] > b[index_b]:
            a[index_merged] = a[index_a]
            index_a -= 1
        else:
            a[index_merged] = b[index_b]
            index_b -= 1
        index_merged -= 1

    return a

