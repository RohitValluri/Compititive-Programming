# Recursion-Only recursion_secondlargest(L) [15 pts]
# Note: recall that you may not use sort, sorted, min, or max this week! With that in mind, write the function 
# recursion_secondlargest(L) that takes x list of integers in any order and returns the second-largest value in the list. To 
# be more precise, it returns the second value from the end if the list was sorted (though you do not need to sort 
# it to solve this problem), so if the largest value occurs twice, you would return that value. Also, if there are 
# fewer than 2 values in the list, return None. Here are some test cases:
# assert(recursion_secondlargest([1,2,3,4,5]) == 4)
# assert(recursion_secondlargest([4,3]) == 3)
# assert(recursion_secondlargest([4,4,3]) == 4)
# assert(recursion_secondlargest([-3,-4]) == -4)
# assert(recursion_secondlargest([4]) == None)
# assert(recursion_secondlargest([ ]) == None)
# Again, you do not need to sort the list. We didn't sort it in our sample solution. We just tracked the two largest 
# values as we recursively traversed the list. Also, you may not use loops/iteration in this problem

from collections import Counter
def recursion_secondlargest(L):
	# Your code goes here
    count=Counter(L)
    # Your code goes here
    if len(L)<=1:
        return None
    
    def recursion(L,i,k,l):
        if (i<(len(L))):

            x = abs(L[i-1])
            y = abs(L[i])
            if (x > y):
                if (y > k):
                    l.remove(k)
                    k = y
                    l.append(k)
                L.remove(L[i])
                recursion(L,i,k,l)
            elif (y > x):
                if (x > k):
                    l.remove(k)
                    k = x
                    l.append(k)
                L.remove(L[i-1])
                recursion(L,i,k,l)
            else:
                return x
        if (L[0]>l[0] and count[L[0]]==1):          
            return l[0]
        elif (l[0]>L[0]):
            return L[0]
        else: 
            return L[0]
    i=1
    k=0
    l=[]
    l.append(k)
    return (recursion(L,i,k,l))

# print(recursion_secondlargest([5,4,5]))
# print(recursion_secondlargest([1,2,3,4,5]))
# print(recursion_secondlargest([4,4,3]))
