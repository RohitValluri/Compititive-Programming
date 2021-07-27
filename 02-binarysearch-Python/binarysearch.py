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
    # Your code goes here
    low = input_array[0]
    high = len(input_array)-1 #assigning last element of array as high

    while low <= high:
  
        middle = (low + high)// 2 #calulating the middle value of the array
          
        if input_array[middle] == value:
            return middle
  
        elif input_array[middle] < value: # if middle value is less than the given value we will ignore the left half of the middle value 
            low = middle + 1

        else:
            high = middle - 1 # if middle value is greater than the given value we will ignore the right half of the middle value
      
    return -1 # if value doesn't exist return -1
    # pass

# print(binary_search([1,10,15,18,24,40,50], 15))
# print(binary_search([1,10,15,18,24,40,50], 40))
# print(binary_search([1,10,15,18,24,40,50], 47))
