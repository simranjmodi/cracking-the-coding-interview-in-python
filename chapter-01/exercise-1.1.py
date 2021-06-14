"""
1.1 Is Unique

Implement an algorithm to determine if a string has all unique characters.
"""

def is_unique_chars(str):
    if len(str) > 128:
        return False

    char_set = [0]*128
    for i in range(len(str)):
        if char_set[ord(str[i])-65]:
            return False
        else:
            char_set[ord(str[i]) - 65] = True
    return True


