"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""
    length = len(input_array)
    out = None
    while length > 1:
        middle = int(length / 2)
        less = input_array[middle-1]
        more = input_array[middle]
        if value < less:
            input_array = input_array[0:middle-1]
            length = len(input_array)
        elif value > more:
            input_array = input_array[middle:]
            length = len(input_array)
        elif value == less:
            out = middle - 1 + length -1
            break
        elif value == more:
            out = middle + length -1
            break
        else:
            break
    if out:
        return out
    else:
        return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print (binary_search(test_list, test_val1))
print (binary_search(test_list, test_val2))