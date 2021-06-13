"""
1.2 Check Permutation:

Given two strings, write a method to decide if one is a permutation of the other.
Assuming comparison is case sensitive and whitespace is significant.

Solution 1

"""

def sort(s):
    sorted_char = sorted(s)
    sorted_str = "".join(sorted_char)
    return sorted_str

def permutation(s,t):
    if len(s) != len(t):
        return False
    else:
        return sort(s) == sort(t)

