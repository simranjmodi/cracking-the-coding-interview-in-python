"""
1.4 Palindrome Permutation

Given a string, write a function to check if it is a permutation of
a palindrome. A palindrome is a word or phrase that is the same
forwards and backwards. A permutation is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary words.

Solution 2: Using bit vector to keep track of letters
"""

def can_permute_palindrome(s: str) -> bool:
    result = 0
    for c in s:
        result ^= 1 << ord(c)

    return result & (result - 1) == 0

