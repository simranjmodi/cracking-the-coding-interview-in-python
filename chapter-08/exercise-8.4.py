"""
8.4 Power Set

Write a method to print all subsets of a set.
"""

import math

def print_power_set(set):
    set_size = len(set)
    pow_set_size = (int)(math.pow(2, set_size))

    for counter in range(0, pow_set_size):
        for j in range(0, set_size):
            if ((counter & (1 << j)) > 0):
                print(set[j], end="")
        print("")
