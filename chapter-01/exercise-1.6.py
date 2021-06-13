"""
1.6 String Compression

Implement a method to perform basic string compression using the counts of
repeated characters. For example, the string aabcccccaaa would become
a2b1c5a3. If the "compressed" string would not become smaller than the
original string, your method should return the original string. You can assume
the string has only uppercase and lower case letters (a-z).

"""

def compress(string):
    n = len(string)
    i = 0
    res = ""
    while i < n - 1:
        count = 1
        while (i < n - 1 and
               string[i] == string[i + 1]):
            count += 1
            i += 1
        i += 1
        res += string[i-1]
        res += str(count)

    return res
