# recusive binarySearchValues(L, v) [20 pts] [autograded]
# Write the recursive function binarySearchValues(L, v) that takes a sorted list L and a value v and returns a list 
# of tuples, (index, value), of the values that binary search must check to verify whether or not v is in L. As an 
# example, say:
#    L = ['a', 'c', 'f', 'g', 'm', 'q']
#    v = 'c'
# Binary search always searches between some lo and hi index, which initially are 0 and (len(L)-1). So here, lo=0 
# and hi=5. The first index we try, then, is middle=2 (the integer average of lo and hi). The value there is 'f', so we 
# will add (2, 'f') to our result.
# Since 'f' is not the value we are seeking, we continue, only now we are searching from lo=0 to hi=1 (not hi=2 
# because we know that index 2 was too high!).
# Now we try middle=0 (the integer average of lo and hi), and so we add (0, 'a') to our result.
# We see that 'a' is too low, so we continue, only now with lo=1 and hi=1. So we add (1, 'c') to our result. We 
# found 'c', so we're done. And so we see:
#     L = ['a', 'c', 'f', 'g', 'm', 'q']
#     v = 'c'
#     assert(binarySearchValues(L, v) == [(2,'f'), (0,'a'), (1,'c')])
# Hint: Do not slice the list L, but rather adjust the indexes into L. 

def recursion_binarysearchvalues(L, v):
    def binarySearch (L, low, high, v):
      
        if high >= low:
            middle = low + (high - low) // 2 #calculating the the middle value of list
            if L[middle] == v:    
                x.append((middle,L[middle])) #if middle value equals to the the required value i am appending the value and index into a list
            elif L[middle] > v:
                x.append((middle,L[middle])) 
                return binarySearch(L, low, middle-1, v) #if middle value is greater than the required value doing recursive binary search in the left part of the array
            else:
                x.append((middle,L[middle]))
                return binarySearch(L, middle + 1, high, v) #if middle value is less than the required value doing recursive binary search in the right part of the array
        return x
    x=[]
    return (binarySearch(L, 0, len(L)-1, v))


# print(recursion_binarysearchvalues(['a', 'c', 'f', 'g', 'm', 'q'], "a"))
# print(recursion_binarysearchvalues(['a', 'c', 'f', 'g', 'm', 'q'], "c"))
# print(recursion_binarysearchvalues(['a', 'c', 'f', 'g', 'm', 'q'], "f"))
	
	