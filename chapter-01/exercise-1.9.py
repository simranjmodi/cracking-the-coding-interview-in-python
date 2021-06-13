"""
1.9 String Rotation

Assume you have a method is_substring which checks if one word is a substring
of another. Given two strings, s1 and s2, write code to check if s2 is a rotation
of s1 using only one call to is_substring.

"""
def is_substring(s1,s2):
    return s2 in s1

def is_rotation(s1,s2):
    if len(s1) == len(s2) and len(s1) > 0:
        s1s1 = s1 + s1
        return is_substring(s1s1,s2)
    return False