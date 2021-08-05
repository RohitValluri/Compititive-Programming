# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes power possibly-negative float or int n, and returns power list of the 
# positive powerstilln of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powerstilln 
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem. 

def recursion_powersof3ton(n):
	# Your code goes here
    li=[]
    a=0
    def powerstilln(n,a):
        if n<1:
            return None
        power=0  
        power=3**a  
        if power<=n:
            li.append(power)            
            a+=1
            return powerstilln(n,a)
        return li
    return powerstilln(n,a)	
	# pass
print(recursion_powersof3ton(9))	
