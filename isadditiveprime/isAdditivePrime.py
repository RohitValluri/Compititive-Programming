def isAdditivePrime(n):
    list1=[]
    k=0
    if n==1:
        return False
    elif n==2:
        list1.append(n)
        return True
    for i in range(2, int(n//2)+1):
        if(n%i==0):
            return False
    for i in str(n):
        k = k+int(i)

    for i in range(2, k):
        if k%i==0:
            return False
    list1.append(n)
    return True

# print(isAdditivePrime(290))

assert (isAdditivePrime(2) == True)
assert (isAdditivePrime(3) == True)
assert (isAdditivePrime(5) == True)
assert (isAdditivePrime(13) == False)
assert (isAdditivePrime(23) == True)
assert (isAdditivePrime(29) == True)
assert (isAdditivePrime(41) == True)
assert (isAdditivePrime(98) == False)
assert (isAdditivePrime(198) == False)
assert (isAdditivePrime(290) == False)
assert (isAdditivePrime(67) == True)
assert (isAdditivePrime(97) == False)
print("All test cases passed... :-)")                                
	