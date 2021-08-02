# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def isproperty309(n):
    x = str(n**5)
    for i in range(10):
        if str(i) in x:
            # print("i:",i)
            continue
        else:
            return False
    return True            
    pass
def nthwithproperty309(n):
    # Your code goes here
    count = 0
    x = 0
    y = 1
    while(n+1!=x):
        if(isproperty309(y)):
            x+=1
            count = y
        y+=1        
    return count

# print(property309(418))
print(nthwithproperty309(0))
print(nthwithproperty309(1))
print(nthwithproperty309(2))