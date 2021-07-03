"""
5.2 Binary to String

Given a real number between 0 and 1 (e.g 0.72) that is passed in as a double,
print the binary representation. If the number cannot be accurately represented
in binary with at most 32 characters, print "ERROR"

Solution 1: Multiply the decimal by 2
"""


def print_binary(n):
    # Check if the number is Between 0 to 1 or Not
    if (n >= 1 or n <= 0):
        return "ERROR"

    answer = ""
    frac = 0.5
    answer = answer + "."

    # Setting a limit on length: 32 characters.
    while (n > 0):

        # Setting a limit on length: 32 characters
        if (len(answer) >= 32):
            return "ERROR"

        # Multiply n by 2 to check it 1 or 0
        b = n * 2
        if (b >= 1):

            answer = answer + "1"
            n = b - 1

        else:
            answer = answer + "0"
            n = b

    return answer


