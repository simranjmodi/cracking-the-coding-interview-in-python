"""
1.4 Palindrome Permutation

Given a string, write a function to check if it is a permutation of
a palindrome. A palindrome is a word or phrase that is the same
forwards and backwards. A permutation is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary words.

Solution 1: Using hash table to count # of times each character appears
"""

def check_max_one_odd(table):
    found_odd = False
    for i in table:
        if i % 2 == 1:
            if found_odd:
                return False
            found_odd = True
    return True

def build_char_freq_table(phrase):
    char_set = [0]*128
    phrase = phrase.replace(" ","")
    for char in phrase:
        char_set[ord(char.lower()) - 65] += 1
    return char_set

def is_permutation_of_palindrome(phrase):
    table = build_char_freq_table(phrase)
    return check_max_one_odd(table)

