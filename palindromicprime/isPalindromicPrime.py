def isPrime(n):
    if n>1:
        for i in range(2, int(n/2)+1):
            if(n%i==0):
                break
        else:
            return True
    else:
        return False            

def isPalindrome(n):
    n=str(n)
    if(n==n[::-1]):
        return True
    else:
        return False 

def isPalindromicPrime(n):
    if (isPrime(n)==True and isPalindrome(n)== True):
        return True
    else:
        return False    

# print(isPalindromicPrime(10))
# print(isPalindrome(14))
# print(isPrime(18))

assert (isPalindromicPrime(2) == True)
assert (isPalindromicPrime(10) == False)
assert (isPalindromicPrime(104) == False)
assert (isPalindromicPrime(235) == False)
assert (isPalindromicPrime(131) == True)
assert (isPalindromicPrime(900) == False)
assert (isPalindromicPrime(101) == True)
assert (isPalindromicPrime(383) == True)
assert (isPalindromicPrime(373) == True)
assert (isPalindromicPrime(121) == False)
print("All test cases passed... :-)")