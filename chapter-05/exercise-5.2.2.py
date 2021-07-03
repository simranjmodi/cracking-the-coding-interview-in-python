"""
5.2 Binary to String

Given a real number between 0 and 1 (e.g 0.72) that is passed in as a double,
print the binary representation. If the number cannot be accurately represented
in binary with at most 32 characters, print "ERROR"

Solution 2: Comparing number to .5, then .25, and so on
"""


def print_binary(n):
    # Check if the number is Between
    # 0 to 1 or Not
    if (n >= 1 or n <= 0):
        return "ERROR"

    frac = 0.5
    answer = "."

    # Setting a limit on length: 32 characters.
    while (n > 0):

        # 32 char max
        if (len(answer) >= 32):
            return "ERROR"

        # compare the number to .5
        if (n >= frac):
            answer += "1"
            n = n - frac
        else:
            answer += "0"

        frac = (frac / 2)

    return answer
