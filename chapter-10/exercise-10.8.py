"""
10.8 Find Duplicates

You have an array with all the numbers from 1 to N, where N is at most
32,000. The array may have duplicate entries and you do not know what N
is. With only 4 kilobytes of memory available, how would you print all
duplicate elements in the array?
"""

class BitArray:
    def __init__(self, n):
        self.arr = [0] * ((n >> 5) + 1)

    def get(self, pos):
        self.index = pos >> 5
        self.bitNo = pos & 0x1F
        return (self.arr[self.index] &
                (1 << self.bitNo)) != 0

    def set(self, pos):
        self.index = pos >> 5
        self.bitNo = pos & 0x1F
        self.arr[self.index] |= (1 << self.bitNo)

def check_duplicates(arr):
    ba = BitArray(32000)

    for i in range(len(arr)):
        num = arr[i]
        if ba.get(num):
            print(num)
        else:
            ba.set(num)
