"""
8.1 Triple Step

A child is running up a staircase with n steps and can hop either 1 step,
2 step or 3 steps at a time. Implement a method to count how many possible
ways the child can run up the stairs.

Solution 1: Simple exponential implementation
"""

def count_ways(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return count_ways(n-1) + count_ways(n-2) + count_ways(n-3)



