"""
1.2 Check Permutation:

Given two strings, write a method to decide if one is a permutation of the other.
Assuming comparison is case sensitive and whitespace is significant.

Solution 2: Optimal approach checking if two strings have identical character counts
"""

def permuation(s,t):
    if len(s) != len(t):
        return False

    letters = [0]*128
    for i in range(len(s)):
        letters[ord(s[i])-65] += 1

    for i in range(len(t)):
        letters[ord(t[i])-65] -= 1
        if letters[ord(t[i])-65] < 0:
            return False

    return True

