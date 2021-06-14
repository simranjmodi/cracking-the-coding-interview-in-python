"""
2.5 Sum Lists

You have two numbers represented by a linked list, where each node
contains a single digit. The digits are stored in reverse order,
such that the 1's digit is at the head of the list. Write a function
that adds the two numbers and returns the sum as a linked list.

Solution 1
"""

# TO FIX

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Add contents of two linked lists and return the head
    # node of resultant list
    def addTwoLists(self, first, second):
        prev = None
        temp = None
        carry = 0

        # While both list exists
        while (first is not None or second is not None):

            # Calculate the value of next digit in
            # resultant list
            # The next digit is sum of following things
            # (i) Carry
            # (ii) Next digit of first list (if ther is a
            # next digit)
            # (iii) Next digit of second list ( if there
            # is a next digit)
            fdata = 0 if first is None else first.data
            sdata = 0 if second is None else second.data
            Sum = carry + fdata + sdata

            # update carry for next calculation
            carry = 1 if Sum >= 10 else 0

            # update sum if it is greater than 10
            Sum = Sum if Sum < 10 else Sum % 10

            # Create a new node with sum as data
            temp = Node(Sum)

            # if this is the first node then set it as head
            # of resultant list
            if self.head is None:
                self.head = temp
            else:
                prev.next = temp

            # Set prev for next insertion
            prev = temp

            # Move first and second pointers to next nodes
            if first is not None:
                first = first.next
            if second is not None:
                second = second.next

        if carry > 0:
            temp.next = Node(carry)

    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


# Driver code
first = LinkedList()
second = LinkedList()

# Create first list
first.push(6)
first.push(1)
first.push(7)
print("First List is ")
first.printList()

# Create second list
second.push(2)
second.push(9)
second.push(5)
print("\nSecond List is ")
second.printList()

# Add the two lists and see result
res = LinkedList()
res.addTwoLists(first.head, second.head)
print("\nResultant list is ")
res.printList()